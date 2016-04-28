include Math

#UI创建
plugins_menu = UI.menu("Plugins")#实例化 菜单栏
 submenu = plugins_menu.add_submenu("3D模型数据采集")#在插件 添加 一级按钮
 submenu.add_item("开始采集") {#添加二级按钮
   UI.messagebox(getRotate)#调用方法
 }


#3d算法
 def getRotate()#定义获取3D转化成2D的方法

    mod = Sketchup.active_model#首先会检索当前的模型对象，然后设置mod等于模型对象。
    ent=mod.entities#回当前一个Entities(实体)对象，包括了当前设计中的所有图形
    sel = mod.selection#一组当前选中实体。使用模型。选择方法选择


    phibeg = 0.0 if not phibeg #距离 变量初始化（或者说是放大的倍数=》有效中心点距离截图位置的距离）

    phiend = 0 if not phiend #角度 变量初始化

    stepw = 0 if not stepw #俯角 变量初始化


    prompts = ["距离", "角度", "俯角"] #label提示标签

    values = [phibeg, phiend, stepw] #赋值 将input的值赋值给变量？

    results = inputbox prompts, values, "3D模型转化2D图片集合" #视图展示第一个参数弹窗类型input框  第二个参数label提示字符 第三个赋值给input标签

    phibeg, phiend, stepw = results #将输入的值返回给变量

    distance=5000 #定位相机初始位置
    target = [0, 0, 0] #截图目标终点
    up = [0, 0, 1] #截图起点

    view = Sketchup.active_model.active_view #激活窗口（打开窗口）



    dirAngle=0#图片水平截图的起始位置
    overAngle=0#图片上下的截图的起始位置

    #创建存放图片的文件夹
    filecheck = File.directory?'c:\rotate'#检查rotate文件是否纯在
    if !filecheck then#不存在创建rotate文件夹
      Dir.mkdir("c:/rotate")
    end

    while distance>=0

      while dirAngle<=360#360度截图（水平角度）

        while overAngle<90#球体的一面角度（上下角度）

          #下面三行简单说就是定位照相机位置 距离*角度
          z=distance*sin(overAngle/180.0*3.14)#定位z轴方位
          x=distance*cos(overAngle/180.0*3.14)*sin(dirAngle/180.0*3.14)#定位x轴位置
          y=distance*cos(overAngle/180.0*3.14)*cos(dirAngle/180.0*3.14)#定位y轴位置

          eye = [x,y,z]#相机 截图位置

          cam = Sketchup::Camera.new eye, target, up#调用sketup的相机工具

          view.camera = cam#生成视图

          view.invalidate#视图数据检测

          view.write_image 'c:\\rotate\\'+dirAngle.to_s+"_"+overAngle.to_s+".jpg"#输出图片文件路径 第一个参数水平角度  第二个产参数上下角度

          overAngle+=5#上下角度偏移量（每次加5）

        end
          overAngle=0#
          dirAngle+=5#水平角度偏移量（每次加5）
      end 
        distance-=100#由远到近（每次-100）
    end
  
 end
