from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
import time

edge_options = EdgeOptions()
edge_options.use_chromium = True
edge_options.add_argument('disable-gpu')                    

edge = Edge(options=edge_options)
edge.get("http://game.ioxapp.com/eye-test/")

edge.implicitly_wait(10)

play_btn = edge.find_element_by_class_name("play-btn")
play_btn.click()

time.sleep(1)

def clickRightButton():
    try:
        box = edge.find_element_by_id("box")
        buttons = box.find_elements_by_tag_name("span")
        buttons.sort(key=lambda k: k.get_attribute("style"),reverse = True)
        buttons[0].click()
        try:
            buttons[len(buttons)-1].click()
        except:
            x = 0
        clickRightButton()
    except:
        return

clickRightButton()