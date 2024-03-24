from pynput import mouse, keyboard
import time

m_crtl = mouse.Controller()
m_button = mouse.Button
print(m_crtl.position)
min_loc = (1805, 5)
crm_tab = (462, 1057)
search_pos = (167, 54)
m_crtl.position = crm_tab
m_crtl.click(m_button.left)
time.sleep(1)
m_crtl.position = search_pos
m_crtl.click(m_button.left)