import numpy as np


class GPA(object):
    
    def __init__(self, grades, sws):
        self.grades = grades
        self.sws = sws
        self.sws_sum = np.sum(sws)
        self.american = self.americanisation(self.grades)
        self.gpa = self.get_GPA(self.american)
        self.style = "Direkt"
                
    @staticmethod
    def americanisation(grades):
        return np.subtract(5, grades)    
    
    @staticmethod
    def weighting(val1, val2):
        return val1 * val2
        
    def get_GPA(self, grades):
        weighted = np.sum(self.weighting(grades, self.sws))
        return np.divide(weighted, self.sws_sum)
    
    def results(self, label):
        out_GPA = float(np.round(self.gpa*100)/100)
        print(f'GPAs für {label} \n {self.style}: {out_GPA}')
        
        
class R_GPA(GPA):
    
    def __init__(self, grades, sws):
        super(R_GPA, self).__init__(grades, sws)
        self.rounding()
        self.american = self.americanisation(self.grades)
        self.gpa = self.get_GPA(self.american)
        self.style = "Gerundet"
        
    @staticmethod
    def rounder(decimal):
        int_dec = int(np.round(decimal*10))
        if int_dec > 7:
            int_dec = 0
        elif int_dec > 3:
            int_dec = 7
        elif int_dec > 0:
            int_dec = 3
        else:
            int_dec = 0
        return float(int_dec)/10
        
    def rounding(self):
        grade_integer = np.floor(self.grades)
        grade_decimal = self.grades % 1
        decimal_rounded = np.asarray(list(map(self.rounder, grade_decimal)))
        self.grades = grade_integer + decimal_rounded
        
        
"""
grades_hf = np.array([2.5, 1.5, 1.65, 2.0, 1.7, 1.7, 1.3, 1.7, 2.5, 2.15, 2.3, 1.7, 1.7, 1.7, 1.0])
sws_hf = np.array([9,9,9,9,9,9,9,9,9,9,9,9,3,4,4])

grades_nf = np.array([2.7,2.0,1.7,3.7,2.0])
sws_nf = np.array([12,12,6,6,6])
"""

"""
Susanne
"""

"""
grades_new = np.array([1.5, 1.65, 2.00, 1.7, 1.3, 1.7, 2.5, 2.15, 2.3, 1.7,
              2.7, 2.0, 1.7, 3.7, 2.0])
ects_new = np.array([9, 9, 9, 9, 9, 9 ,9, 9, 9, 9,
           12, 12, 6, 6, 6])

grades_singular = np.array([1.7, 1.3, 2., 1.3, 2., 2., 1.7, 1.3, 1.7, 3.0, 2.0, 2.0, 2.3, 2.3, 1.7,
                            2.7, 3.0, 2.0, 2.7, 1.7, 3.7, 2])

ects_singular = np.array([3, 2, 3, 2, 3, 2, 6, 6, 6, 2, 3, 2, 2, 6, 6,
                          4, 4, 4, 4, 4, 4, 4])
"""

"""
Thede Master

grades_master = np.array([2.3, 1.3, 1.3, 2, 1, 1.7, 2.3, 1.7, 2.3, 1.7, 2.3, 2.3, 2.7, 1.7])
ects_master = np.array([9, 30, 6, 2, 6, 3, 3, 6, 4, 6, 3, 6, 4, 30])


Thede Bachelor

grades_bachelor = np.array([3, 3.7, 2.3, 3.5, 3.7, 2, 3, 4, 1.8, 3.1, 1.6, 1.5, 2.5, 2.3, 1.3, 2])
ects_bachelor = np.array([7, 8, 7, 10, 8, 8, 8, 8, 10, 10, 8, 12, 12, 8, 4, 12])
"""

"""
Susanne Bachelor
"""
grades_hfach = np.array([
            1.5, 1.65, 2.0, 1.7, 1.3, 1.7, 2.5, 2.15, 2.3, 1.7, 1.7, 1.3, 1.7
            ])
grades_nfach=np.array([
            2.7, 2.0, 1.7, 3.7, 1.3, 2.5, 2.3
            ])

ects_hfach = np.array([
            9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
            12, 12])
ects_nfach = np.array([
            12, 12, 6, 6, 6, 12, 6
            ])

# assert grades_master.shape == ects_master.shape
assert grades_hfach.shape == ects_hfach.shape
assert grades_nfach.shape == ects_nfach.shape
# assert grades_nf.shape == sws_nf.shape

# master_direkt = GPA(grades_master, ects_master)
# master_rounded = R_GPA(grades_master, ects_master)

grades_main = GPA(grades_hfach, ects_hfach)
grades_main_rounded = R_GPA(grades_hfach, ects_hfach)


grades_side = GPA(grades_nfach, ects_nfach)
grades_side_rounded = R_GPA(grades_nfach, ects_nfach)

grades_total = GPA(np.append(grades_hfach, grades_nfach), np.append(ects_hfach, ects_nfach))
grades_total_rounded = R_GPA(np.append(grades_hfach, grades_nfach), np.append(ects_hfach, ects_nfach))

grades_total.results("Hauptfach + Nebenfach")
grades_main.results("Hauptfach")
grades_side.results("Nebenfach")

grades_total_rounded.results("Hauptfach + Nebenfach")
grades_main_rounded.results("Hauptfach")
grades_side_rounded.results("Nebenfach")

print("\n Noten \n Hauptfach: \n")
print(f'Noten \n D.: {grades_main.grades} \n A.: {grades_main.american}')
print(f'LP \n {ects_hfach}')
print("\n Nebenfach: \n")
print(f'Noten \n D.: {grades_side.grades} \n A.: {grades_side.american}')
print(f'LP \n {ects_nfach}')