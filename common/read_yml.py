
import yaml
import os

class ReadYaml():
    def __init__(self,yamlPath=r"\conf\testdata.yml"):
        self.yamlPath = yamlPath

    #获取yaml文件的地址
    def getpath(self):
        #获取当前文件所在的目录地址
        current_dir = os.path.abspath(".")
        #获取当前脚本的地址
        #curPath = os.path.realpath(__file__)
        #获取db.yaml的地址,即用上一级的目录地址加上yamlPath
        path = os.path.dirname(current_dir) + self.yamlPath
        return path

    #读取yaml文件
    def readyaml(self):
        path = self.getpath()
        '''读取yaml文件内容
           参数path: 相对路径，起始路径：项目的根目录
           realPath: 文件的真实路径,绝对路径地址 '''
        if not os.path.isfile(path):
            raise FileNotFoundError("文件路径不存在，请检查路径是否正确：%s" % path)
        with open(path, 'r', encoding='utf-8') as f:
            y = f.read()
            d = yaml.load(y, Loader=yaml.FullLoader)
        return d

if __name__ == '__main__':
    ry = ReadYaml().readyaml()
    print(ry)
    #print(ry['test_add_param_demo'])