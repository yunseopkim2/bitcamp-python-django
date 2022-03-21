import numpy as np
import pandas as pd
from icecream import ic
from context.models import Model
from context.domains import Dataset
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier


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
        this =self.drop_feature(this, 'SibSp', 'Parch', 'Cabin', 'Ticket')
        #self.kwargs_sample(name ='이순신')
        this = self.extract_title_from_name(this)
        title_mapping = self.remove_duplicate(this)
        this = self.title_nominal(this, title_mapping)
        this = self.drop_feature(this, 'Name')
        this = self.sex_nominal(this)
        this = self.drop_feature(this, 'Sex')
        this = self.embarked_nominal(this)
        this = self.age_ratio(this)
        this = self.drop_feature(this, 'Age')
        this = self.pclass_ordinal(this)
        this = self.fare_ratio(this)
        this = self.drop_feature(this, 'Fare')
        self.df_info(this)
        k_fold = self.create_k_fold()
        accurary = self.get_accuracy(this, k_fold)

        ic(accurary)

        return this

    def learning(self, train_fname, test_fname):
        k_fold = self.create_k_fold()
        this = self.preprocess(train_fname, test_fname)
        ic(f'사이킷런 알고리즘 정확도: {self.get_accuracy(this, k_fold)}')
        self.submit(this)

    @staticmethod
    def submit(this):
        clf = RandomForestClassifier()
        clf.fit(this.train, this.label)
        prediction = clf.predict(this.test)
        pd.DataFrame({'PassengerId': this.id, 'Survived': prediction}).to_csv('./save/submission.csv', index=False)

    @staticmethod
    def df_info(this):
        [print(f'{i.info()}') for i in [this.train, this.test]]
        ic(this.train.head(5))
        ic(this.test.head(5))

    @staticmethod
    def null_check(this):
        [ic(f'{i.isnull().sum()}') for i in [this.train, this.test]]

    @staticmethod
    def id_info(this):
        ic(f'id 의 타입  {type(this.id)}')
        ic(f'id 의 상위 3개 {this.id[:3]}')

    @staticmethod
    def drop_feature(this, *feature) -> object:
        '''i for i in feature:
            this.train = this.train.drop(a, axis=1)
            this.test = this.test.drop(a, axis=1)

            for i in [this.train, this.test]:
                for j in feature:
                i.drop(j, axis=1, inplace = True)
            '''

        [j.drop(list(feature), axis=1, inplace=True) for j in [this.train, this.test]]
        # [i.drop(j, axis =1, inplace=True) for j in feature for i in [this.train, this.test] ]

        return this

    @staticmethod
    def kwargs_sample(**kwargs) -> None:
        ic(type(kwargs))
        print({''.join(f'key:{i}, val:{j}') for i, j in kwargs.items()})
        '''
           Categorical vs. Quantitative
           Cate -> nominal (이름) vs. ordinal (순서)
           Quan -> interval (상대) vs. ratio (절대)
           '''

    @staticmethod
    def name_nominal(this) -> object:
        combine = [this.train, this.test] # 데이터셋에 형태를 리스트 형태로 담아 편집하려한다.
        for datset in combine:
            datset['Title'] = datset.Name.str.extract('([A-Za-z]+)\.',expand=False) # 정규식, 각 캐리터의 옵션 대소문자가 반드시 있어야한다.
            ic(datset['Title'])

        return this

    @staticmethod
    def extract_title_from_name(this) -> object:
        # 데이터셋에 형태를 리스트 형태로 담아 편집하려한다.
        for these in [this.train, this.test]:
            these['Title'] = these.Name.str.extract('([A-Za-z]+)\.', expand=False)
            # ic(this.train.head(5))
        return this

    @staticmethod
    def remove_duplicate(this) -> None:
        a = []
        for these in [this.train, this.test]:
            a += list(set(these['Title']))
        a = list(set(a))
        #print(f'>>>>{a}')
        '''
        >>>>['Col', 'Countess', 'Dona', 'Mlle', 'Mme', 'Dr',
             'Don', 'Ms', 'Lady', 'Mrs', 'Capt', 'Miss', 'Jonkheer',
            'Rev', 'Major', 'Sir', 'Mr', 'Master']
            Royal : ['Countess', 'Lady', 'Sir']
            Rare : ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme']
            Mr : ['Mlle']
            Ms : ['Miss']
            Master
            Mrs
        '''
        title_mapping = {'Mr': 1, 'Ms': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        return title_mapping

    @staticmethod
    def title_nominal(this, title_mapping) -> object:
        for these in [this.train, this.test]:
            these['Title'] = these['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            these['Title'] = these['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
            these['Title'] = these['Title'].replace(['Mlle'], 'Mr')
            these['Title'] = these['Title'].replace(['Miss'], 'Ms')
            these['Title'] = these['Title'].fillna(0)
            these['Title'] = these['Title'].map(title_mapping)
        return this

    @staticmethod
    def pclass_ordinal(this) -> object:
        pclass_mapping = {'1': 1, '2':2, '3':3}

        for these in [this.train, this.test]:
            these = these.fillna({'Pclass': '3'})
            these['Pclass'] = these['Pclass'].map(pclass_mapping)
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        gender_mapping = {'male': 0, 'female': 1}
        for these in [this.train, this.test]:
            these['Gender'] = these['Sex'].map(gender_mapping)
        return this

    @staticmethod
    def age_ratio(this) -> object:
        train = this.train
        test = this.test
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
                       'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]  # scaling
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        for these in train, test:
            # pd.cut() 을 사용하시오. 다른 곳은 고치지 말고 다음 두 줄만 코딩하시오
            these['AgeGroup'] = pd.cut(these['Age'], bins, labels=labels)  # pd.cut() 을 사용 [데이터, 구간의 갯수, 레이블명]
            these['AgeGroup'] = these['AgeGroup'].map(age_mapping)  # map() 을 사용
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        embarkes_mapping = {'S': 1, 'C': 2, 'Q': 3}
        this.train = this.train.fillna({'Embarked': 'S'})  # 임의로 널 값을 S항선지로 넣는것이다.
        for these in [this.train, this.test]:
            these['Embarked'] = these['Embarked'].map(embarkes_mapping)

        return this

    @staticmethod
    def fare_ratio(this) -> object:
        fare_mapping = {1, 2, 3, 4}
        bins = [-1, 8, 15, 31, np.inf]
        labels = ['4등급', '3등급', '2등급', '1등급']

        for these in [this.train, this.test]:
            these['FareBand'] = these['Fare'].fillna(1)
            these['FareBand'] = pd.qcut(these['FareBand'], 4, fare_mapping)

        return this

    @staticmethod
    def create_k_fold() -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0)

    @staticmethod
    def get_accuracy(this, k_fold):
        score = cross_val_score(RandomForestClassifier(), this.train, this.label,
                                cv=k_fold, n_jobs=1, scoring='accuracy')
        return round(np.mean(score)*100, 2)  # round 반올림



