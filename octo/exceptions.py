class OctoException(Exception):
	pass


class NotStartedError(OctoException):
	"""Raised when trying to call octo.stop before octo.start"""
	pass


class AlreadyStartedError(OctoException):
	"""Raised when trying to call octo.start more than once"""
	pass
