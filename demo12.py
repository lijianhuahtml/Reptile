from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# 动作链

# drag_and_drop()方法
#
# 在上面的实例中，一些交互动作都是针对某个节点执行的。比如，对于输入框，我们就调用它的输入文字和清空文字方法；对于按钮，就调用它的点击方法。其实，还有另外一些操作，
# 它们没有特定的执行对象，比如鼠标拖曳、键盘按键等，这些动作用另一种方式来执行，那就是动作链。
#
# 比如，现在实现一个节点的拖曳操作，将某个节点从一处拖曳到另外一处

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
log = browser.find_element(By.XPATH, '//div[@id="iframewrapper"]/iframe')
browser.switch_to.frame(log)
source = browser.find_element(By.CSS_SELECTOR,'#draggable')
target = browser.find_element(By.CSS_SELECTOR,'#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()

# drag_and_drop()方法涉及到参数传递，一个是要拖拽元素的起点，一个是要拖拽元素的终点
#
# 首先，打开网页中的一个拖曳实例，然后依次选中要拖曳的节点和拖曳到的目标节点，
# 接着声明 ActionChains 对象并将其赋值为 actions 变量，然后通过调用 actions 变量的 drag_and_drop() 方法，
# 再调用 perform() 方法执行动作，此时就完成了拖曳操作

