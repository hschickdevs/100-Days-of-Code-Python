import os


if __name__ == "__main__":
    print("Generating directory structure ...")
    for i in range(1, 100, 10):
        dir = f'days{i:03d}-{i + 9:03d}'
        print(i, dir)
        os.mkdir(dir)
        
        # Generate subfolders
        for j in range(i, i + 10):
            subdir = f'{dir}/day{j:03d}'
            print(j, subdir)
            os.mkdir(subdir)
            
    print("Done!")