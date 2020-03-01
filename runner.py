import os, shutil

src_dir = 'cifar100-generated'
tgt_dir = 'cifar100-original'
no_of_fakes = [100, 200, 300, 400, 500]
for i, n in enumerate(no_of_fakes):
    for d in os.listdir(src_dir):
        src = os.path.join(src_dir, d)
        dst = os.path.join(tgt_dir, d)
        if os.path.isdir(src):
            files = sorted(os.listdir(src))[n-100:n]
            files = [os.path.join(src, f) for f in files]
            for f in files:
                shutil.copy(f, dst)
    print(f'Copied {n} generated images')
    os.system(f'python train.py -net resnet50 | tee output_resnet50_augdata{n}.txt')