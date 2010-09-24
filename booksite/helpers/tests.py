# -*- coding: utf-8 -*-

from datetime import datetime, date, timedelta

from django.core.exceptions import ValidationError
from django.test import TestCase

from helpers.validators import YoungerThen, OlderThen, in_future, in_past


class ValidatorsTest(TestCase):
    def test_in_future(self):
        self.assertRaises(ValidationError,
                          in_future,
                          datetime.now() - timedelta(days=1))
        try:
            in_future(datetime.now() + timedelta(days=1))
        except ValidationError:
            self.fail('in_future raise ValidationError on now() + timedelta')

    def test_in_past(self):
        self.assertRaises(ValidationError,
                          in_past,
                          datetime.now() + timedelta(days=1))
        try:
            in_past(datetime.now() - timedelta(days=1))
        except ValidationError:
            self.fail('in_past raise ValidationError on now() - timedelta')

    def test_younger_then(self):
        v = YoungerThen(18)
        self.assertRaises(ValidationError,
                          v,
                          date.today() - timedelta(days=20*365))
        try:
            v(date.today() - timedelta(days=15*365))
        except ValidationError:
            self.fail("YoungerThen(18) raises ValidationError on 15 years")


    def test_older_then(self):
        v = OlderThen(18)
        self.assertRaises(ValidationError,
                          v,
                          date.today() - timedelta(days=15*365))
        try:
            v(date.today() - timedelta(days=20*365))
        except ValidationError:
            self.fail("OlderThen(18) raises ValidationError on 20 years")
