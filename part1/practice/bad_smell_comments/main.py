# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    # ...
    def mvmntobjbfld(self, field, x_axis, y_axis, field_2_param, direction, is_fly: bool, is_crowl: bool, points_per_action = 1):
        """Функция реализует перемещение юнита по полю. в качестве параметров принимает текущие координаты юнита, 
        направление его движения, состояние не летит ли он, состояние не крадется ли он и базовый параметр скорости с 
        которым двигается юнит
        :param field: поле по которому перемещается юнит
        :param feld_1_param: x-координата юнита
        :param field_2_param: у- координата юнита
        :param direction: направление перемещения
        :param is_fly: летит ли юнит
        :param is_crowl: крадется ли юнит
        :param points_per_action: базовый параметр скорости
        """
        if is_fly and is_crowl: 
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            points_per_action *= 1.2 
            if direction == 'UP':
                new_y = y_axis + points_per_action
                new_x = x_axis
            elif direction == 'DOWN':
                new_y = y_axis - points_per_action
                new_x = x_axis
            elif direction == 'LEFT':  
                new_y = y_axis
                new_x = x_axis - points_per_action 
            elif direction == 'RIGHT':  
                new_y = y_axis
                new_x = x_axis + points_per_action 


        if is_crowl:
            points_per_action *= 0.5
            if direction == 'UP':
                new_y = y_axis + points_per_action
                new_x = x_axis
            elif direction == 'DOWN':
                new_y = y_axis - points_per_action
                new_x = x_axis
            elif direction == 'LEFT':
                new_y = y_axis
                new_x = x_axis - points_per_action
            elif direction == 'RIGHT':
                new_y = y_axis
                new_x = x_axis + points_per_action

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
