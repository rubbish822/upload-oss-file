# coding: utf-8
import typing

import oss2
from uploadOss.upload_oss_file import (
    UploadOssFile, unquote_gbk,
)


def upload_file(
        file_path: str,
        doc_ext: str = 'xls',
        acl: typing.Any = oss2.OBJECT_ACL_PUBLIC_READ,
        if_have_key: str = '1',
        doc_name: str = ''
) -> typing.Any:
    """
    上传文件到oss
    :param file_path: 文件路径
    :param doc_ext: 文件后缀名
    :param acl: 文件权限
    :param if_have_key: 是否需要自定义key（文件名称）, 为1时, 则使用原文件名称, 否则生成uuid4随机名称
    :param doc_name: 原始文件的名称（上传时的名称）
    """
    upload_oss = UploadOssFile()
    file_url = upload_oss.upload_to_oss(
        file_path, doc_ext=doc_ext, acl=acl,
        if_have_key=if_have_key, doc_name=doc_name
    )
    return unquote_gbk(file_url)
