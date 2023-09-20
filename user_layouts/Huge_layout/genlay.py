import os
import shutil

path = "E:/FILES/GitHub/LPHK/user_layouts/Huge_layout"

def copy_sm(dest):
    shutil.copy(os.path.join(path, "smolmain.lpl"), dest)

def copy_temp(dest, h_ind, s_ind, r_ind, n_ind):
    source_path = path+"/template.lpl"
    dest = os.path.join(path, f'huge_{h_ind}', f'smol_{s_ind}', f'row_{r_ind}', f'{n_ind}.lpl')
    if os.path.exists(source_path):
        shutil.copy(source_path, dest)
        print(f'File {n_ind}.lpl copied from {source_path} to {dest}')
    else:
        print(f"File not found: {source_path}")

for i in range(1, 9):
    huge = f'huge_{i}'
    huge_path = os.path.join(path, huge)
    os.makedirs(huge_path)

    for j in range(1, 9):
        smol = f'smol_{j}'
        smol_path = os.path.join(huge_path, smol)
        os.makedirs(smol_path)

        for k in range(1, 9):
            row = f'row_{k}'
            row_path = os.path.join(smol_path, row)
            os.makedirs(row_path)

            for l in range(1, 9):
                n = f'{l}'
                n_path = os.path.join(row_path, n)
                copy_temp(n_path, i,j,k,l)

    copy_sm(huge_path)
