#include <iostream>
#include <memory.h>

const long long BUFFER_SIZE = 5.5 * 1024 * 1024 * 1024; // 5 GB

int main(int argc, char *argv[])
{
    // // malloc of size BUFFER_SIZE
    // char *mmap_ptr = reinterpret_cast<char *>(malloc(BUFFER_SIZE));
    // if (mmap_ptr == nullptr)
    // {
    //     perror("malloc");
    //     return -1;
    // }
    // std::cout << "Buffer pointer: " << static_cast<void *>(&mmap_ptr) << std::endl;

    // memset(mmap_ptr, 0, BUFFER_SIZE);

    // std::cout << "Press enter to continue..." << std::endl;
    // std::cin.get();

    // // free the buffer
    // free(mmap_ptr);

    // std::cout << "Memory freed" << std::endl;

    // return 0;
    int i, n, size;
    int *a;

    printf("Number of calloc: ");
    scanf("%d", &n);
    printf("Size of calloc(in bytes): ");
    scanf("%d", &size);
    std::cin.get();

    int **x = (int **)calloc(n, sizeof(int *));
    for (i = 0; i < n; i++)
    {
        x[i] = (int *)malloc(size);
        if (x[i] == NULL)
        {
            perror("malloc failed");
            return -1;
        }
        memset(x[i], 0, size);
        printf("calloc %d bytes memory.\r\n", size);
    }
    printf("done\r\n");
    std::cout << "Press enter to continue..." << std::endl;
    std::cin.get();
    return 0;
}
