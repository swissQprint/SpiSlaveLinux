#obj-m := hello.o
#obj-m+= spi-slave-debug.o spi-slave-core.o spi-slave-dev.o spi-mcspi-slave.o 
obj-m+=  spi-mcspi-slave.o 

#ADD_CFLAGS += -g -DDEBUG
#ccflags-y += ${ADD_CFLAGS}
#CC += ${ADD_CFLAGS}
SRC := $(shell pwd)
#SLAVE_SRC := slave_app.c

all:
	$(MAKE) -C $(KERNEL_SRC) M=$(SRC)

#debug:
#	$(MAKE) -C $(KERNEL_SRC) M=$(SRC) modules EXTRA_CFLAGS="$(ADD_CFLAGS)"

modules_install:
	$(MAKE) -C $(KERNEL_SRC) M=$(SRC) modules_install

clean:
	rm -f *.o *~ core .depend .*.cmd *.ko *.mod.c
	rm -f Module.markers Module.symvers modules.order
	rm -rf .tmp_versions Modules.symvers

#slave_app:
#	.echo $(MAKE) -o slave_app $(SLAVE_SRC)
#	$(MAKE) $(SLAVE_SRC) -o slave_app
