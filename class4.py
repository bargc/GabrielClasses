import numpy as np
import pandas as pd
import save_files_functions as sff

example_list = [
    [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
]


#print sum(example_list) / float(len(example_list))
sqrt_list = np.sqrt(example_list[0]).tolist()


example_list.append(sqrt_list)


if __name__ == '__main__':
    #sff.write_to_file(content, 'test2.gab', 'w')
    sff.write_to_csv(example_list, 'test1.csv', 'wb')#b=binary





