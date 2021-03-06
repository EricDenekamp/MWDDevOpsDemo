# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Edu Team
# All rights reserved.
#

from mwddevopsdemo_ext.extension import MwddevopsdemoExtension


def test_process_asset_purchase_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = MwddevopsdemoExtension(client, logger, config)
    result = ext.process_asset_purchase_request(request)
    assert result.status == 'success'


def test_process_asset_change_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = MwddevopsdemoExtension(client, logger, config)
    result = ext.process_asset_change_request(request)
    assert result.status == 'success'


def test_process_asset_cancel_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = MwddevopsdemoExtension(client, logger, config)
    result = ext.process_asset_cancel_request(request)
    assert result.status == 'success'


def test_process_asset_adjustment_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = MwddevopsdemoExtension(client, logger, config)
    result = ext.process_asset_adjustment_request(request)
    assert result.status == 'success'


def test_validate_asset_purchase_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = MwddevopsdemoExtension(client, logger, config)
    result = ext.validate_asset_purchase_request(request)
    assert result.status == 'success'
    assert result.data == request


def test_validate_asset_change_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = MwddevopsdemoExtension(client, logger, config)
    result = ext.validate_asset_change_request(request)
    assert result.status == 'success'
    assert result.data == request


def test_process_product_custom_event(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = MwddevopsdemoExtension(client, logger, config)
    result = ext.process_product_custom_event(request)
    assert result.status == 'success'
    assert result.http_status == 200
    assert result.headers is None
    assert result.body is None


def test_process_new_listing_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1, 'type': 'type', 'state': 'state'}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = MwddevopsdemoExtension(client, logger, config)
    result = ext.process_new_listing_request(request)
    assert result.status == 'success'


def test_process_remove_listing_request(
    sync_client_factory,
    response_factory,
    logger,
):
    config = {}
    request = {'id': 1, 'type': 'type', 'state': 'state'}
    responses = [
        response_factory(count=100),
        response_factory(value=[{'id': 'item-1', 'value': 'value1'}]),
    ]
    client = sync_client_factory(responses)
    ext = MwddevopsdemoExtension(client, logger, config)
    result = ext.process_remove_listing_request(request)
    assert result.status == 'success'
