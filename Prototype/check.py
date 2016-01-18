import subprocess
import os

inparanoid_loc = r"C:\Users\csiddarth\Source\Repos\Prototype\Prototype\m_incognita\inparanoid_4.1"
ip_pl = os.path.join(inparanoid_loc, "inparanoid.pl")
param1 = os.path.join(inparanoid_loc,"c_elegans_p.fa")
param2 = os.path.join(inparanoid_loc,"m_incognita_g.fa")

pipe = subprocess.Popen([r"C:\Strawberry\perl\bin\perl",ip_pl,param1,param2])


#subprocess.call(["ls", "-l", "/etc/resolv.conf"])

