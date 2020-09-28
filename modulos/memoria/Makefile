obj-m := memoria.o

CC	= gcc
CFLAGS-y	= -g
all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD)
modulesclean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean