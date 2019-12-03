# 两种方式导入package中模块，在init文件中加入from. import...
# 或者直接from package import...

from DL_33_package_sample import send_massage as SM
from DL_33_package_sample import rec_massage as RM
SM.send_massage()
RM.rec_massage()

import DL_33_package_sample as PS
PS.send_massage.send_massage()
PS.rec_massage.rec_massage()