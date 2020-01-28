

char x[0x10000] __attribute__((section(".duhh"))) __attribute__((aligned(8))) = {0};

int main() {
    while (1) {}
    return 0;
}
