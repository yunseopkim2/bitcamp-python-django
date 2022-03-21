# https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
from icecream import ic
from titanic.views import TitanicView
from titanic.models import TitanicModel
from titanic.template import TitanicTemplate

if __name__ == '__main__':
  # view = TitanicView()


    while 1:

        menu = input('1.전처리 2.템플릿')
        if menu == '1':
            ic(' #### 1.전처리 #### ')
            # view.preprocess('train.csv','test.csv')
            template = TitanicTemplate(fname='train.csv')
            template.visualize()

            break

        elif menu == '2':
            print('### 2.템플릿 ###')
            model = TitanicModel()
            model.learning(train_fname='train.csv', test_fname='test.csv')
            break

        else:

            break