# https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
from icecream import ic

from titanic.views import TitanicView
from titanic.models import TitanicModel
if __name__ == '__main__':
    view = TitanicView()
    model = TitanicModel(train_fname='train.csv',
                         test_fname='test.csv')
    while 1:

        menu = input('1.전처리')
        if menu == '1':
            ic(' #### 1. 전처리 #### ')
            # view.preprocess('train.csv','test.csv')

            model.__init__('train.csv','test.csv')
            break
        else:
            break