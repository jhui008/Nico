import os
import time

from nico.nico import AdbAutoNico


# nico(text ="Add another email account").wait_for_appearance()
# nico(text ="Set up your personal or work email").wait_for_appearance()
# nico(text ="Network & internet").wait_for_appearance()
# nico(text ="Bluetooth").wait_for_appearance()
# nico(text ="Connected devices").wait_for_appearance()
# nico(text ="Display").wait_for_appearance()
# nico(text ="Sound").wait_for_appearance()
# nico(text ="Sound").click()
# nico(text="Do Not Disturb").click()
#
start_time = time.time()

#
# commands = f"""adb -s 22367209daba64b1 shell am instrument -w -e class hank.dump_hierarchy.HierarchyTest hank.dump_hierarchy.test/androidx.test.runner.AndroidJUnitRunner"""
# # 替换为你要执行的外部命令

nico = AdbAutoNico("22367209daba64b1")

nico(text ="Next").wait_for_appearance()

nico(text ="Next").click()



end_time = time.time()
print("代码执行时间：", end_time - start_time, "秒")
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()
# nico(text ="声音和振动").wait_for_appearance()

#
#
# # dump_ui_xml("emulator-5554")
# # import time
#

