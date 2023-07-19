#include <sys/socket.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <sys/un.h>
#include <fcntl.h>
#include <unistd.h>

ssize_t
read_fd(int fd, void *ptr, size_t nbytes, int *recvfd)
{
    struct msghdr msg;
    struct iovec iov[1];
    ssize_t n;
    // int newfd;

    // #ifdef HAVE_MSGHDR_MSG_CONTROL
    union
    {
        struct cmsghdr cm;
        char control[CMSG_SPACE(sizeof(int))];
    } control_un;
    struct cmsghdr *cmptr;

    msg.msg_control = control_un.control;
    msg.msg_controllen = sizeof(control_un.control);
    // #else
    //     msg.msg_accrights = (caddr_t)&newfd;
    //     msg.msg_accrightslen = sizeof(int);
    // #endif

    msg.msg_name = NULL;
    msg.msg_namelen = 0;

    iov[0].iov_base = ptr;
    iov[0].iov_len = nbytes;
    msg.msg_iov = iov;
    msg.msg_iovlen = 1;

    if ((n = recvmsg(fd, &msg, 0)) <= 0)
        return (n);

    // #ifdef HAVE_MSGHDR_MSG_CONTROL
    if ((cmptr = CMSG_FIRSTHDR(&msg)) != NULL &&
        cmptr->cmsg_len == CMSG_LEN(sizeof(int)))
    {
        if (cmptr->cmsg_level != SOL_SOCKET)
            perror("control level != SOL_SOCKET");
        if (cmptr->cmsg_type != SCM_RIGHTS)
            perror("control type != SCM_RIGHTS");
        *recvfd = *((int *)CMSG_DATA(cmptr));
    }
    else
        *recvfd = -1; /* descriptor was not passed */
                      // #else
                      //     /* *INDENT-OFF* */
                      //     if (msg.msg_accrightslen == sizeof(int))
                      //         *recvfd = newfd;
                      //     else
                      //         *recvfd = -1; /* descriptor was not passed */
                      //                       /* *INDENT-ON* */
                      // #endif

    return (n);
}
/* end read_fd */

// main function, create unix socket from path passed in argv, accept connection and read the file descriptor
// from the socket, then read the file and print it to stdout
int main(int argc, char **argv)
{
    int listenfd, connfd;
    socklen_t clilen;
    struct sockaddr_un cliaddr, servaddr;
    char buf[1024];
    int fd;

    listenfd = socket(AF_LOCAL, SOCK_STREAM, 0);

    unlink(argv[1]);

    bzero(&servaddr, sizeof(servaddr));
    servaddr.sun_family = AF_LOCAL;
    strcpy(servaddr.sun_path, argv[1]);

    bind(listenfd, (struct sockaddr *)&servaddr, sizeof(servaddr));

    listen(listenfd, 5);
    clilen = sizeof(cliaddr);
    connfd = accept(listenfd, (struct sockaddr *)&cliaddr, &clilen);

    read_fd(connfd, buf, 1, &fd);

    read(fd, buf, 1024);
    printf("%s", buf);

    lseek(fd, 0, SEEK_SET);
    write(fd, "Hola Mundo!", 11);

    return 0;
}