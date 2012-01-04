from melopy import Melopy
import os

def main():
    m = Melopy('furelise')
    m.parse(os.path.dirname(__file__) + '/meeps/furelise.mp')
    m.render()
    
if __name__ == '__main__':
    main()