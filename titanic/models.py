from icecream import ic
from context.models import Model
from context.domains import Dataset


class TitanicModel(object):
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname):
        this = self.dataset
        that = self.model
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']
        this.train = this.train.drop(['Survived'], axis=1)  # 1 = 열(세로) 0 = 행(가로)

        self.drop_feature(this, 'SibSp', 'Parch', 'Cabin', 'Ticket')

        this = self.drop_feature(this)
        '''
       
        this = self.create_label(this)
        this = self.create_train(this)
        this = self.create_label(this)
        this = self.name_nominal(this)
        this = self.sex_nominal(this)
        this = self.age_ratio(this)
        this = self.fare_ratio(this)
        this = self.pclass_ordinal(this)
        this = self.embarked_nominal(this)
        '''
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('*'*100)
        ic(f'1. Train의 타입 : {type(this.train)}\n')
        ic(f'2. Train의 컬럼 : {this.train.columns}\n')
        ic(f'3. Train의 상위 1개 : {this.train.head(1)}\n')
        ic(f'4. Train의 null의 개수 : {this.train.isnull().sum()}\n')
        ic(f'5. Test의 타입 : {type(this.test)}\n')
        ic(f'6. Test의 컬럼 : {this.test.columns}\n')
        ic(f'7. Test의 상위 1개 : {this.test.head(1)}\n')
        ic(f'8. Test의 null의 개수 : {this.test.isnull().sum()}\n')
        ic(f'8. 의 타입 : {type(this.id)}\n')
        ic(f'8. 의 상위 10개 : {this.id[:10]}\n')
        print('*'*100)

    def creat_this(self, dataset) -> object:
        this = dataset
        this.train = self.train
        this.test = self.test
        this.id = self.id
        return this

    @staticmethod
    def drop_feature(this, *feature) -> None:
        a = [i for i in feature]

        this.train = this.train.drop(a, axis=1)
        this.test = this.test.drop(a, axis=1)

        return this

    @staticmethod
    def create_train(this) -> object:
        return this

    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def name_nominal(this) -> object:
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        return this

    @staticmethod
    def age_ratio(this) -> object:
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        return this