#include <linux/proc_fs.h>
#include <linux/seq_file.h>
#include <asm/uaccess.h>
#include <linux/hugetlb.h>
#include <linux/module.h>
#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/fs.h>

#define BUFESIZE    150
struct sysinfo inf;

static int my_proc_show(struct seq_file *m,void *v){
    si_meminfo(&inf);
    seq_printf(m, "\"RAM Total\": \t%li\n", (inf.totalram*4)/(1024));
    seq_printf(m, " \"RAM Libre:\" \t%li\n", (inf.freeram*4)/(1024));
    seq_printf(m, "\"RAM en uso\": \t%li %%\n",((inf.totalram-inf.freeram)*100)/inf.totalram);
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