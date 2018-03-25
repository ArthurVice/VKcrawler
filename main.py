# coding: utf-8
import vk
import csv
import unicodecsv as csv
import time

vk_domain = raw_input("Please Enter Public Page Name:")

########################################################################################################################


def get_vk_likes(vk_attachments):
    likes = vk_attachments['likes']['count']
    return likes


def get_vk_reposts(vk_attachments):
    reposts = vk_attachments['reposts']['count']
    return reposts


def get_vk_attachments(vk_attachments):  # Returns attachments; Only photo yet
    if vk_attachments.get('attachments') is None:
        return 'None'
    elif vk_attachments['attachments'][0]['type'] == 'photo':
        attachments = vk_attachments['attachments'][0]['type'] + " " + vk_attachments['attachments'][0]['photo']['src']
        return attachments
    else:
        return 'None'



def get_vk_comments(vk_attachments):
    comments = vk_attachments['comments']['count']
    return comments


def get_vk_text(vk_attachments):
    text = vk_attachments['text']
    return text


def create_string_for_csv(vk_attachments):
    string = get_vk_text(vk_attachments) + ', ' + str(get_vk_attachments(vk_attachments)) + ', ' + str(
        get_vk_likes(vk_attachments)) + ', ' + str(get_vk_comments(vk_attachments)) + ', ' + str(
        get_vk_reposts(vk_attachments))

    return string

########################################################################################################################


def main():
    session = vk.AuthSession(app_id='6271287', user_login='375447070551', user_password='92qc31mf')  # AUTHORIZATION.
    api = vk.API(session)
    vk_data= api.wall.get(domain=vk_domain, count='100', filter='all', extended='1', v='4.9')  # TARGET

    vk_something = vk_data['wall']

    time_now = time.strftime("%Y-%m-%d %H%M")
    vk_domain_and_time = str(time_now) + ' ' + vk_domain

    with open('%s vk_data_input.csv' % vk_domain_and_time, 'wb') as csv_file:
        default_in = [vk_domain_and_time, ' 100', ' all', ' 1']  # Writes default input data
        writer = csv.writer(csv_file, encoding='utf-8')
        writer.writerow(['Time' + 'Domain' + 'Count' + 'Filter' + 'Extended'])
        writer.writerow(default_in)

    with open('%s vk_data_out.csv' % vk_domain_and_time,  'wb') as csv_file:  # Writes a parsed data into csv
            writer = csv.writer(csv_file, encoding='utf-8')
            writer.writerow([' Text', ' Attachments', ' Likes', ' Comments', ' Reposts'])
            for item in vk_something[1:]:
                csv_list = list([create_string_for_csv(item)])  # Can be tuple or list
                writer.writerow(csv_list)


if __name__ == '__main__':
    main()
