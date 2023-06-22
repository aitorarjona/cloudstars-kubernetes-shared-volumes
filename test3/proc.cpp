#include <cstring>
#include <fcntl.h>
#include <iostream>
#include <unistd.h>
#include <sys/mman.h>
#include <openssl/md5.h>
#include <iostream>
#include <iomanip>
#include <sstream>

const long long MEM_PAGE_SIZE = 4 * 1024;              // 4 KB
const long long BUFFER_SIZE = MEM_PAGE_SIZE * 2621440; // 10 GB

int main(int argc, char *argv[])
{
    int fd = open("/tmp/large_file.txt", O_RDWR, S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP);
    if (fd == -1)
    {
        perror("open");
        return -1;
    }

    char *mmap_ptr =
        reinterpret_cast<char *>(mmap(nullptr, BUFFER_SIZE, PROT_WRITE, MAP_SHARED, fd, 0));
    std::cout << "Buffer pointer: " << static_cast<void *>(&mmap_ptr) << std::endl;

    std::cout << "Press enter to continue..." << std::endl;
    std::cin.get();

    unsigned char md5_checksum[MD5_DIGEST_LENGTH];

    MD5_CTX md5_context;
    MD5_Init(&md5_context);
    MD5_Update(&md5_context, mmap_ptr, BUFFER_SIZE);
    MD5_Final(md5_checksum, &md5_context);

    std::stringstream ss;
    for (int i = 0; i < MD5_DIGEST_LENGTH; i++)
    {
        ss << std::hex << std::setw(2) << std::setfill('0') << static_cast<int>(md5_checksum[i]);
    }
    std::cout << "MD5 checksum: " << ss.str() << std::endl;

    int res = munmap(mmap_ptr, BUFFER_SIZE);
    if (res == -1)
    {
        perror("munmap");
        return -1;
    }
    std::cout << "munmap " << res << std::endl;

    res = close(fd);
    if (res == -1)
    {
        perror("close");
        return -1;
    }
    std::cout << "close " << res << std::endl;

    close(fd);
}
