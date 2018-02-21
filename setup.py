import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\Administrator\\Anaconda3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Administrator\\Anaconda3\\tcl\\tk8.6"

executable = [cx_Freeze.Executable("pygamer.py")]

cx_Freeze.setup(
	name = "Monero to the Moon",
	options = {
		"build exe": {"packages":["pygame"],
		"include_files":["C:\\Users\\Administrator\\Desktop\\pygamer\\img\\XMR.png","C:\\Users\\Administrator\\Desktop\\pygamer\\img\\icon.png", "C:\\Users\\Administrator\\Desktop\\pygamer\\img\\blockImg.png", "C:\\Users\\Administrator\\Desktop\\pygamer\\img\\moonero.png", "C:\\Users\\Administrator\\Desktop\\pygamer\\img\\starcloud.jpg", "C:\\Users\\Administrator\\Desktop\\pygamer\\img\\shitcoin.png", "C:\\Users\\Administrator\\Desktop\\pygamer\\img\\shitcoin1.png", "C:\\Users\\Administrator\\Desktop\\pygamer\\music\\TRAPFORD.wav", "C:\\Users\\Administrator\\Desktop\\pygamer\\highscore.txt"]}},
	executables = executable,
	version = "1.0.0"


	)