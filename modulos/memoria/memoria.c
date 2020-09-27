#include <linux/fs.h>
#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/hugetlb.h>
#include <linux/module.h>
#include <linux/proc_fs.h>
#include <linux/seq_file.h>



static int my_proc_show(struct seq_file *m,void *v){
    struct sysinfo info;
    si_meminfo(&info); 
	unsigned long mem_total = ((info.totalram*info.mem_unit) / 1024) / 1024; 
	unsigned long mem_libre = ((info.freeram*info.mem_unit) / 1024) / 1024; 
	int utilizado = ((mem_total - mem_libre) * 100) / mem_total;     
    seq_printf(m, "{\n");
    seq_printf(m, "\"total\": %lu,\n",mem_total);
    seq_printf(m, " \"libre\": %lu,\n", mem_libre);
    seq_printf(m, "\"uso\": %i \n}",utilizado);
    
    return 0;
} 


static ssize_t my_proc_write(struct file* file,const char __user *buffer, size_t count,loff_t *f_pos){
    return 0;
}

static int my_proc_open(struct inode *inode,struct file * file){
    return single_open(file, my_proc_show,NULL);
}


static struct file_operations my_fops = {
    .owner = THIS_MODULE,
    .open = my_proc_open,
    .release = single_release,
    .read = seq_read,
    .llseek = seq_lseek,
    .write = my_proc_write
};

static int __init memoria_init(void){
    struct proc_dir_entry *entry;
    entry = proc_create("memoria-module",0777,NULL,&my_fops);
    if(!entry){
        return -1;
    }else{
        printk(KERN_INFO "Inicio\n");
        return 0;
    }
}


static void __exit memoria_clean(void){
    remove_proc_entry("memoria-module",NULL);
     printk(KERN_INFO "Salida\n");
}


module_init(memoria_init);
module_exit(memoria_clean);
MODULE_LICENSE("GPL");   