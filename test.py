# @author: YuanWei

import os
import sys
import numpy as np
import time
import math
import random
import pickle
import glob

class Test:
    def __init__(self):
        self.test_data = []
        self.test_label = True
    def load_test_data(self):
        print(f"test_label: {self.test_label}")

    def get_name(self, original_name):
        if original_name == "刘本红" or "言" in original_name or "红" in original_name or "俊" in original_name or "瑜" in original_name or "昕" in original_name or "屁" in original_name or "怡" in original_name:
            return f"{original_name}是猪"
        elif "伟" in original_name or "wayne" in original_name or "维" in original_name:
            return f"{original_name}是帅仔"
        else:
            return f"{original_name}是胖仔"
        # return f"{original_name}是猪"



























if __name__ == "__main__":
    test_data = Test()
    # test_data.load_test_data()
    input_data = input("请输入姓名:")
    name = test_data.get_name(input_data)
    print(name)