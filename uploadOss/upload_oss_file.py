# coding: utf-8
import typing
import uuid
import os
import logging
from urllib.parse import unquote

import oss2
from django.conf import settings


logger = logging.getLogger('oss')


class UploadOssFile(object):

    def __init__(
            self: typing.Any,
            oss_key: str=settings.OSS_ACCESS_KEY_ID,
            oss_secret: str=settings.OSS_ACCESS_KEY_SECRET,
            oss_bucket: str=settings.OSS_BUCKET,
            oss_endpoint: str=settings.OSS_ENDPOINT
    ) -> typing.NoReturn:
        self.oss_key = oss_key
        self.oss_secret = oss_secret
        self.oss_bucket = oss_bucket
        self.oss_endpoint = oss_endpoint

    def create_oss_bucket(self: typing.Any, connect_timeout: int=120):
        """
        创建oss bucket
        :return:
        """
        # 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
        bucket = oss2.Bucket(
            oss2.Auth(self.oss_key, self.oss_secret),
            self.oss_endpoint,
            self.oss_bucket,
            connect_timeout=connect_timeout
        )
        return bucket

    def upload_to_oss(
            self,
            file_path: str,
            doc_ext: str='xls',
            acl: typing.Any=oss2.OBJECT_ACL_PUBLIC_READ,
            if_have_key: str='1',
            doc_name: str=''
    ) -> typing.Any:
        """
        :param file_path:
        :param doc_ext: 文件后缀名
        :param acl: 文件权限
        :param if_have_key: 是否需要自定义key（文件名称）
        :param doc_name: 原始文件的名称（上传时的名称）
        :return:
        """
        # 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
        bucket = self.create_oss_bucket()
        if if_have_key == '1':
            # 表示使用原文件名称,注意文件名称是汉字时，上传之后会变成乱码，存储文件地址的地方需要转换为utf-8编码
            # from urllib.parse import unquote
            # file_url = unquote(file_url, encoding='utf-8')
            key = doc_name
        else:
            key = str(uuid.uuid4()).lower() + doc_ext
        ret = bucket.put_object_from_file(key, file_path)
        bucket.put_object_acl(key=key, permission=acl)
        if ret.status == 200 and ret.resp.status == 200 and ret.resp.response.url:
            # 删除服务器上面已经上传的文件
            if os.path.exists(file_path):
                os.remove(file_path)
            return ret.resp.response.url
        logger.error(f'oss upload error: {file_path}')
        return ''


def unquote_gbk(string: str) -> typing.Any:
    """
    将乱码转换为汉字
    :param string:
    :return:
    """
    return unquote(string, encoding='utf-8')
