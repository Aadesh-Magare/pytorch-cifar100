import os, shutil

src_dir = 'cifar100-generated'
tgt_dir = 'cifar100-original'
no_of_fakes = [100, 200, 300, 400, 500]
for i, n in enumerate(no_of_fakes):
    for dir in os.listdir(src_dir):
        if os.path.isdir(dir):
            s = os.path.join(src_dir, dir)
            d = os.path.join(tgt_dir, dir)
        
            files = sorted(os.listdir(s))[n-100:n]

            for f in files:
                shutil.copy(f, d)

    os.system(f'python train.py -net resnet50 | tee output_resnet50_augdata{n}.txt')