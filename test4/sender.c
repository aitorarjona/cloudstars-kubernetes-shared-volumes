#include <sys/socket.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <sys/un.h>
#include <fcntl.h>
#include <unistd.h>

ssize_t write_fd(int fd, void *ptr, size_t nbytes, int sendfd)
{
    struct msghdr msg;
    struct iovec iov[1];

    // #ifdef HAVE_MSGHDR_MSG_CONTROL
    union
    {
        struct cmsghdr cm;
        char control[CMSG_SPACE(sizeof(int))];
    } control_un;
    struct cmsghdr *cmptr;

    msg.msg_control = control_un.control;
    msg.msg_controllen = sizeof(control_un.control);

    cmptr = CMSG_FIRSTHDR(&msg);
    cmptr->cmsg_len = CMSG_LEN(sizeof(int));
    cmptr->cmsg_level = SOL_SOCKET;
    cmptr->cmsg_type = SCM_RIGHTS;
    *((int *)CMSG_DATA(cmptr)) = sendfd;
    // #else
    //     msg.msg_accrights = (caddr_t)&sendfd;
    //     msg.msg_accrightslen = sizeof(int);
    // #endif

    msg.msg_name = NULL;
    msg.msg_namelen = 0;

    iov[0].iov_base = ptr;
    iov[0].iov_len = nbytes;
    msg.msg_iov = iov;
    msg.msg_iovlen = 1;

    return (sendmsg(fd, &msg, 0));
}

// main function, get target socket path and file path to send trough argv, open both to get the file descriptors
// and send the file descriptor of the file to the socket
int main(int argc, char **argv)
{
    int sockfd;
    struct sockaddr_un servaddr;
    int fd;
    char buf[1024];

    if (argc != 3)
    {
        printf("usage: %s <socket_path> <file_path>\n", argv[0]);
        exit(1);
    }

    sockfd = socket(AF_LOCAL, SOCK_STREAM, 0);

    bzero(&servaddr, sizeof(servaddr));
    servaddr.sun_family = AF_LOCAL;
    strcpy(servaddr.sun_path, argv[1]);

    connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr));

    fd = open(argv[2], O_RDWR);
    write_fd(sockfd, "", 1, fd);

    printf("Press enter to continue...\n");
    getchar();
    lseek(fd, 0, SEEK_SET);
    read(fd, buf, 1024);
    printf("%s", buf);

    return 0;
}