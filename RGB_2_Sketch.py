from cv2 import cv2
import myutils
import argparse
import os
'''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image to be scanned")
args = vars(ap.parse_args())
'''
def rgb_to_sketch(pic_name):
	#img_rgb = cv2.imread(args["image"])
	img_rgb = cv2.imread(pic_name)
	#print(img_rgb.shape)
	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)##转为灰度图
	##可改变图片的尺寸，只设置h或者只设置w就会按照等比例放大或缩小；若都指定，则按照指定的大小变换
	img_gray=myutils.resize(img_gray, height = 500)
	img_blur = cv2.GaussianBlur(img_gray, ksize=(21, 21), sigmaX=0, sigmaY=0)##高斯滤波
	##可改变scale的值来改变生成效果，scale越小，会让一些原本比较亮的区域变得更加清晰
	img_blend = cv2.divide(img_gray, img_blur, scale=225)##图像相除实现素描效果
	return img_blend
def convert_batch(dir_path):
	is_exist=os.path.exists(dir_path)
	if((is_exist==False)):
		print("该文件夹不存在，请输入正确的文件夹路径")
		return
	pic_name_list=os.listdir(dir_path)
	#print(pic_name_list)
	for pic_name in pic_name_list:
		pic_path = dir_path + "/" + pic_name
		img_blend = rgb_to_sketch(pic_path)
		pre_dst_name=pic_name.split('.')[0]
		dst_dir_path=dir_path+"_sketch"
		if not os.path.exists(dst_dir_path):
			os.makedirs(dst_dir_path)
		cv2.imwrite(dst_dir_path+'/'+pre_dst_name+"_sketch.jpg", img_blend)
		print("素描生成成功,图片名字是---%s"%(pre_dst_name+"_sketch.jpg"))
if __name__ == "__main__":
	convert_batch(r"C:\Users\Alex\Desktop\Python_Notes\img_recog\OpenCV\RGB_2_Sketch\av_stars")