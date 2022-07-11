# 第一种写法，通过函数替代元类
def upper_attr(class_name,class_parents,class_attrs):
    # 遍历任何一个类中所有的属性，把非私有的属性名字改成大写
    # 定义一个字典保存改完名字之后的属性集合
    new_attrs = {}
    for name,value in class_attrs.items():
        if not name.startswith('__'): # 判断是否为：非私有的属性
            new_attrs[name.upper()] = value
    # 直接调用type来创建一个类
    return type(class_name,class_parents,new_attrs)
#测试
class Emp(object,metaclass=upper_attr):
    name = '张三'
    acl = 5000
if __name__ == '__main__':
    print(hasattr(Emp,'name')) # 判断Emp类中是否有名字为小写name的属性 False
    print(hasattr(Emp,'NAME')) # 判断Emp类中是否有名字为大写NAME的属性 True
    print(hasattr(Emp,'ACL')) # 判断Emp类中是否有名字为大写ACL的属性 True
