# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 22:20
# @Author  : for
# @File    : 09_poo_copy_test.py
# @Software: PyCharm
import os,shutil,multiprocessing
def copy_work(src_dir,dst_dir,file_name):
    pid = multiprocessing.current_process().pid
    src_file_path = src_dir + file_name
    dst_file_path = dst_dir  + file_name
    print(src_file_path)
    with open(dst_file_path,'ab') as dst_file:
        with open(src_file_path,'rb') as src_file:
        #     while True:
        #         data = src_file.read(1024)
        #         if data:
        #             dst_file.write(data)
        #         else:
        #             break
            while True:
                src_file_data = src_file.read(1024)
                print(src_file_data)
                if src_file_data:
                    dst_file.write(src_file_data)
                else:
                    break
if __name__ == '__main__':
    src_dir = './copy/'
    dst_dir = './copy_in/'
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    os.mkdir(dst_dir)
    file_name_list = os.listdir(src_dir)
    pool = multiprocessing.Pool(3)
    for file_name in file_name_list:

        pool.apply_async(copy_work,(src_dir,dst_dir,file_name))
    pool.close()
    pool.join()