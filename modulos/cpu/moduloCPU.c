#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/fs.h>
#include <linux/proc_fs.h>
#include <linux/seq_file.h>
#include <asm/uaccess.h>
#include <linux/sched/signal.h>
#include <linux/sched.h>
#include <linux/ktime.h>

s64  uptime;
int hz = 100;

struct task_struct *task;
struct task_struct *task_child;
struct list_head *list;

static int my_proc_show(struct seq_file *m,void *v){
    int tiempoTotal = 0;
    int tiempoI=0;
    int segundos = 0;

    for_each_process(task){
        uptime = ktime_divns(ktime_get_coarse_boottime(), NSEC_PER_SEC);
        tiempoTotal = tiempoTotal + task->utime + task->stime;
        tiempoI =  task->start_time;       
        segundos = segundos + (uptime - (tiempoI / hz));
        
        /*
        list_for_each(list, &task->children){                        
            task_child = list_entry( list, struct task_struct, sibling );    
            tiempoTotal = tiempoTotal + task_child->utime +task_child->stime;
        }
        */
        
        
    }
    seq_printf(m, "{\n");
    seq_printf(m, "\"HZ\" : %d ,\n", hz);
    seq_printf(m, "\"tiempo\" : %u ,\n", tiempoTotal);
    seq_printf(m, "\"segundos\": %llu \n", segundos);
    seq_printf(m, " }");
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
    entry = proc_create("cpu-module",0777,NULL,&my_fops);
    if(!entry){
        return -1;
    }else{
        printk(KERN_INFO "Inicio\n");
        return 0;
    }
}


static void __exit memoria_clean(void){
    remove_proc_entry("cpu-module",NULL);
    printk(KERN_INFO "Salida\n");
}


module_init(memoria_init);
module_exit(memoria_clean);
MODULE_LICENSE("GPL");   