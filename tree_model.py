def predict_diabetes(pregnancies=None,
                     glucose=None,
                     blood_pressure=None,
                     skinfold=None,
                     insulin=None,
                     bmi=None,
                     diabetes_pedigree=None,
                     age=None):
    """ Predictor for Diabetes from model/6194fd2f8be2aa39c0003f4e

        Dataset created from a study of diabetes in females 21 years or older and of Pima Indian heritage. 
        Pima Indians are an interesting population to study for diabetes because they have a higher incidence of diabetes than the general U.S. population.
        Source
        Pima Indians Diabetes Data Set[*] 
        Bache, K. & Lichman, M. (2013). UCI Machine Learning Repository[*]. Irvine, CA: University of California, School of Information and Computer Science.
        
        [*]Pima Indians Diabetes Data Set: http://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes
        [*]UCI Machine Learning Repository: http://archive.ics.uci.edu/ml
    """
    if (glucose is None):
        return u'False'
    if (glucose > 120):
        if (glucose > 159):
            if (age is None):
                return u'True'
            if (age > 63):
                return u'False'
            if (age <= 63):
                if (pregnancies is None):
                    return u'True'
                if (pregnancies > 7):
                    return u'True'
                if (pregnancies <= 7):
                    if (blood_pressure is None):
                        return u'True'
                    if (blood_pressure > 92):
                        if (bmi is None):
                            return u'False'
                        if (bmi > 34.25):
                            if (bmi > 39.25):
                                return u'False'
                            if (bmi <= 39.25):
                                return u'True'
                        if (bmi <= 34.25):
                            return u'False'
                    if (blood_pressure <= 92):
                        if (insulin is None):
                            return u'True'
                        if (insulin > 41):
                            if (insulin > 80):
                                if (bmi is None):
                                    return u'True'
                                if (bmi > 44.45):
                                    if (bmi > 52.75):
                                        return u'True'
                                    if (bmi <= 52.75):
                                        return u'False'
                                if (bmi <= 44.45):
                                    if (glucose > 190):
                                        if (blood_pressure > 69):
                                            if (bmi > 36.6):
                                                return u'False'
                                            if (bmi <= 36.6):
                                                return u'True'
                                        if (blood_pressure <= 69):
                                            return u'False'
                                    if (glucose <= 190):
                                        return u'True'
                            if (insulin <= 80):
                                return u'False'
                        if (insulin <= 41):
                            return u'True'
        if (glucose <= 159):
            if (age is None):
                return u'False'
            if (age > 24):
                if (diabetes_pedigree is None):
                    return u'True'
                if (diabetes_pedigree > 0.74975):
                    if (diabetes_pedigree > 1.416):
                        if (bmi is None):
                            return u'False'
                        if (bmi > 41.8):
                            return u'True'
                        if (bmi <= 41.8):
                            return u'False'
                    if (diabetes_pedigree <= 1.416):
                        if (skinfold is None):
                            return u'True'
                        if (skinfold > 42):
                            if (bmi is None):
                                return u'False'
                            if (bmi > 36.3):
                                return u'True'
                            if (bmi <= 36.3):
                                return u'False'
                        if (skinfold <= 42):
                            return u'True'
                if (diabetes_pedigree <= 0.74975):
                    if (bmi is None):
                        return u'True'
                    if (bmi > 47.88333):
                        return u'True'
                    if (bmi <= 47.88333):
                        if (bmi > 30.075):
                            if (age > 34):
                                if (diabetes_pedigree > 0.4305):
                                    if (diabetes_pedigree > 0.694):
                                        if (diabetes_pedigree > 0.726):
                                            return u'True'
                                        if (diabetes_pedigree <= 0.726):
                                            return u'False'
                                    if (diabetes_pedigree <= 0.694):
                                        return u'True'
                                if (diabetes_pedigree <= 0.4305):
                                    if (diabetes_pedigree > 0.1585):
                                        if (pregnancies is None):
                                            return u'True'
                                        if (pregnancies > 1):
                                            if (glucose > 156):
                                                return u'True'
                                            if (glucose <= 156):
                                                if (glucose > 124):
                                                    if (diabetes_pedigree > 0.1975):
                                                        if (diabetes_pedigree > 0.295):
                                                            if (diabetes_pedigree > 0.3965):
                                                                if (bmi > 33.8):
                                                                    return u'True'
                                                                if (bmi <= 33.8):
                                                                    return u'False'
                                                            if (diabetes_pedigree <= 0.3965):
                                                                return u'False'
                                                        if (diabetes_pedigree <= 0.295):
                                                            if (bmi > 33.3):
                                                                if (bmi > 34.45):
                                                                    if (glucose > 141):
                                                                        return u'True'
                                                                    if (glucose <= 141):
                                                                        if (bmi > 35.45):
                                                                            return u'False'
                                                                        if (bmi <= 35.45):
                                                                            return u'True'
                                                                if (bmi <= 34.45):
                                                                    return u'False'
                                                            if (bmi <= 33.3):
                                                                return u'True'
                                                    if (diabetes_pedigree <= 0.1975):
                                                        return u'False'
                                                if (glucose <= 124):
                                                    return u'True'
                                        if (pregnancies <= 1):
                                            return u'True'
                                    if (diabetes_pedigree <= 0.1585):
                                        return u'True'
                            if (age <= 34):
                                if (blood_pressure is None):
                                    return u'False'
                                if (blood_pressure > 67):
                                    if (bmi > 32.75):
                                        if (glucose > 132):
                                            if (blood_pressure > 72):
                                                if (glucose > 157):
                                                    return u'True'
                                                if (glucose <= 157):
                                                    return u'False'
                                            if (blood_pressure <= 72):
                                                return u'True'
                                        if (glucose <= 132):
                                            return u'False'
                                    if (bmi <= 32.75):
                                        if (bmi > 31.4):
                                            return u'True'
                                        if (bmi <= 31.4):
                                            return u'False'
                                if (blood_pressure <= 67):
                                    if (diabetes_pedigree > 0.471):
                                        if (bmi > 35.3):
                                            return u'False'
                                        if (bmi <= 35.3):
                                            return u'True'
                                    if (diabetes_pedigree <= 0.471):
                                        return u'True'
                        if (bmi <= 30.075):
                            if (diabetes_pedigree > 0.2145):
                                if (bmi > 29.4):
                                    return u'False'
                                if (bmi <= 29.4):
                                    if (bmi > 23.4):
                                        if (blood_pressure is None):
                                            return u'True'
                                        if (blood_pressure > 62):
                                            if (glucose > 123):
                                                if (age > 26):
                                                    if (skinfold is None):
                                                        return u'True'
                                                    if (skinfold > 28):
                                                        return u'True'
                                                    if (skinfold <= 28):
                                                        if (skinfold > 25):
                                                            return u'False'
                                                        if (skinfold <= 25):
                                                            if (skinfold > 8):
                                                                return u'True'
                                                            if (skinfold <= 8):
                                                                if (bmi > 26.1):
                                                                    if (diabetes_pedigree > 0.331):
                                                                        return u'True'
                                                                    if (diabetes_pedigree <= 0.331):
                                                                        return u'False'
                                                                if (bmi <= 26.1):
                                                                    return u'True'
                                                if (age <= 26):
                                                    return u'False'
                                            if (glucose <= 123):
                                                return u'False'
                                        if (blood_pressure <= 62):
                                            return u'False'
                                    if (bmi <= 23.4):
                                        return u'False'
                            if (diabetes_pedigree <= 0.2145):
                                return u'False'
            if (age <= 24):
                if (blood_pressure is None):
                    return u'False'
                if (blood_pressure > 55):
                    if (bmi is None):
                        return u'False'
                    if (bmi > 41.375):
                        if (diabetes_pedigree is None):
                            return u'True'
                        if (diabetes_pedigree > 0.7625):
                            return u'False'
                        if (diabetes_pedigree <= 0.7625):
                            if (skinfold is None):
                                return u'True'
                            if (skinfold > 50):
                                return u'False'
                            if (skinfold <= 50):
                                return u'True'
                    if (bmi <= 41.375):
                        if (insulin is None):
                            return u'False'
                        if (insulin > 30):
                            return u'False'
                        if (insulin <= 30):
                            if (glucose > 130):
                                if (glucose > 135):
                                    return u'False'
                                if (glucose <= 135):
                                    if (blood_pressure > 74):
                                        return u'False'
                                    if (blood_pressure <= 74):
                                        return u'True'
                            if (glucose <= 130):
                                return u'False'
                if (blood_pressure <= 55):
                    if (diabetes_pedigree is None):
                        return u'True'
                    if (diabetes_pedigree > 0.239):
                        return u'True'
                    if (diabetes_pedigree <= 0.239):
                        return u'False'
    if (glucose <= 120):
        if (bmi is None):
            return u'False'
        if (bmi > 26.68154):
            if (age is None):
                return u'False'
            if (age > 30):
                if (glucose > 106):
                    if (age > 57):
                        return u'False'
                    if (age <= 57):
                        if (pregnancies is None):
                            return u'True'
                        if (pregnancies > 6):
                            return u'True'
                        if (pregnancies <= 6):
                            if (insulin is None):
                                return u'True'
                            if (insulin > 110):
                                return u'True'
                            if (insulin <= 110):
                                if (bmi > 32.65):
                                    if (blood_pressure is None):
                                        return u'False'
                                    if (blood_pressure > 69):
                                        return u'False'
                                    if (blood_pressure <= 69):
                                        if (blood_pressure > 30):
                                            return u'True'
                                        if (blood_pressure <= 30):
                                            return u'False'
                                if (bmi <= 32.65):
                                    if (blood_pressure is None):
                                        return u'True'
                                    if (blood_pressure > 70):
                                        return u'True'
                                    if (blood_pressure <= 70):
                                        return u'False'
                if (glucose <= 106):
                    if (glucose > 83):
                        if (diabetes_pedigree is None):
                            return u'False'
                        if (diabetes_pedigree > 0.6365):
                            if (diabetes_pedigree > 0.944):
                                if (bmi > 29.75):
                                    return u'False'
                                if (bmi <= 29.75):
                                    return u'True'
                            if (diabetes_pedigree <= 0.944):
                                if (blood_pressure is None):
                                    return u'True'
                                if (blood_pressure > 69):
                                    return u'True'
                                if (blood_pressure <= 69):
                                    if (bmi > 30.45):
                                        return u'False'
                                    if (bmi <= 30.45):
                                        return u'True'
                        if (diabetes_pedigree <= 0.6365):
                            if (blood_pressure is None):
                                return u'False'
                            if (blood_pressure > 71):
                                if (bmi > 39.35):
                                    return u'True'
                                if (bmi <= 39.35):
                                    if (pregnancies is None):
                                        return u'False'
                                    if (pregnancies > 11):
                                        if (skinfold is None):
                                            return u'True'
                                        if (skinfold > 35):
                                            return u'False'
                                        if (skinfold <= 35):
                                            return u'True'
                                    if (pregnancies <= 11):
                                        if (blood_pressure > 75):
                                            if (age > 36):
                                                if (bmi > 34.25):
                                                    if (skinfold is None):
                                                        return u'False'
                                                    if (skinfold > 12):
                                                        if (bmi > 37.4):
                                                            return u'False'
                                                        if (bmi <= 37.4):
                                                            return u'True'
                                                    if (skinfold <= 12):
                                                        return u'False'
                                                if (bmi <= 34.25):
                                                    return u'False'
                                            if (age <= 36):
                                                return u'True'
                                        if (blood_pressure <= 75):
                                            return u'False'
                            if (blood_pressure <= 71):
                                return u'False'
                    if (glucose <= 83):
                        return u'False'
            if (age <= 30):
                if (bmi > 49.14):
                    return u'True'
                if (bmi <= 49.14):
                    if (bmi > 30.565):
                        if (bmi > 45.40833):
                            return u'True'
                        if (bmi <= 45.40833):
                            if (diabetes_pedigree is None):
                                return u'False'
                            if (diabetes_pedigree > 0.66325):
                                if (bmi > 32.7):
                                    if (insulin is None):
                                        return u'False'
                                    if (insulin > 69):
                                        if (skinfold is None):
                                            return u'True'
                                        if (skinfold > 19):
                                            return u'True'
                                        if (skinfold <= 19):
                                            return u'False'
                                    if (insulin <= 69):
                                        if (age > 22):
                                            return u'False'
                                        if (age <= 22):
                                            return u'True'
                                if (bmi <= 32.7):
                                    return u'False'
                            if (diabetes_pedigree <= 0.66325):
                                if (bmi > 38.295):
                                    return u'False'
                                if (bmi <= 38.295):
                                    if (pregnancies is None):
                                        return u'False'
                                    if (pregnancies > 0):
                                        if (bmi > 38.15):
                                            return u'True'
                                        if (bmi <= 38.15):
                                            if (pregnancies > 2):
                                                if (age > 26):
                                                    return u'False'
                                                if (age <= 26):
                                                    if (diabetes_pedigree > 0.27):
                                                        if (bmi > 35.05):
                                                            return u'True'
                                                        if (bmi <= 35.05):
                                                            return u'False'
                                                    if (diabetes_pedigree <= 0.27):
                                                        return u'True'
                                            if (pregnancies <= 2):
                                                return u'False'
                                    if (pregnancies <= 0):
                                        if (glucose > 102):
                                            return u'True'
                                        if (glucose <= 102):
                                            if (bmi > 37.15):
                                                if (bmi > 37.8):
                                                    return u'False'
                                                if (bmi <= 37.8):
                                                    return u'True'
                                            if (bmi <= 37.15):
                                                return u'False'
                    if (bmi <= 30.565):
                        if (pregnancies is None):
                            return u'False'
                        if (pregnancies > 7):
                            return u'True'
                        if (pregnancies <= 7):
                            return u'False'
        if (bmi <= 26.68154):
            if (glucose > 105):
                if (glucose > 107):
                    return u'False'
                if (glucose <= 107):
                    if (blood_pressure is None):
                        return u'False'
                    if (blood_pressure > 65):
                        return u'False'
                    if (blood_pressure <= 65):
                        if (skinfold is None):
                            return u'True'
                        if (skinfold > 24):
                            return u'False'
                        if (skinfold <= 24):
                            return u'True'
            if (glucose <= 105):
                return u'False'
