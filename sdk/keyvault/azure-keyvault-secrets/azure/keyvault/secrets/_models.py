# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from datetime import datetime

from typing import Any, Dict, Optional, Union

from ._generated import models as _models
from ._shared import parse_key_vault_id


class SecretProperties(object):
    """A secret's ID and attributes."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._attributes: Optional[_models.SecretAttributes] = args[0] if args else kwargs.get("attributes", None)
        self._id: Optional[str] = args[1] if len(args) > 1 else kwargs.get("vault_id", None)
        self._vault_id = KeyVaultSecretIdentifier(self._id) if self._id else None
        self._content_type = kwargs.get("content_type", None)
        self._key_id = kwargs.get("key_id", None)
        self._managed = kwargs.get("managed", None)
        self._tags = kwargs.get("tags", None)

    def __repr__(self) -> str:
        return f"<SecretProperties [{self.id}]>"[:1024]

    @classmethod
    def _from_secret_bundle(
        cls, secret_bundle: Union[_models.DeletedSecretBundle, _models.SecretBundle]
    ) -> "SecretProperties":
        return cls(
            secret_bundle.attributes,
            secret_bundle.id,
            content_type=secret_bundle.content_type,
            key_id=secret_bundle.kid,
            managed=secret_bundle.managed,
            tags=secret_bundle.tags,
        )

    @classmethod
    def _from_secret_item(cls, secret_item: Union[_models.DeletedSecretItem, _models.SecretItem]) -> "SecretProperties":
        return cls(
            secret_item.attributes,
            secret_item.id,
            content_type=secret_item.content_type,
            managed=secret_item.managed,
            tags=secret_item.tags,
        )

    @property
    def content_type(self) -> Optional[str]:
        """An arbitrary string indicating the type of the secret.

        :returns: The content type of the secret.
        :rtype: str or None
        """
        return self._content_type

    @property
    def id(self) -> Optional[str]:
        """The secret's ID.

        :returns: The secret's ID.
        :rtype: str or None
        """
        return self._id

    @property
    def key_id(self) -> Optional[str]:
        """If this secret backs a certificate, this property is the identifier of the corresponding key.

        :returns: The ID of the key backing the certificate that's backed by this secret. If the secret isn't backing a
            certificate, this is None.
        :rtype: str or None
        """
        return self._key_id

    @property
    def enabled(self) -> Optional[bool]:
        """Whether the secret is enabled for use.

        :returns: True if the secret is enabled for use; False otherwise.
        :rtype: bool or None
        """
        return self._attributes.enabled if self._attributes else None

    @property
    def not_before(self) -> Optional[datetime]:
        """The time before which the secret cannot be used, in UTC.

        :returns: The time before which the secret cannot be used, in UTC.
        :rtype: ~datetime.datetime or None
        """
        return self._attributes.not_before if self._attributes else None

    @property
    def expires_on(self) -> Optional[datetime]:
        """When the secret expires, in UTC.

        :returns: When the secret expires, in UTC.
        :rtype: ~datetime.datetime or None
        """
        return self._attributes.expires if self._attributes else None

    @property
    def created_on(self) -> Optional[datetime]:
        """When the secret was created, in UTC.

        :returns: When the secret was created, in UTC.
        :rtype: ~datetime.datetime or None
        """
        return self._attributes.created if self._attributes else None

    @property
    def updated_on(self) -> Optional[datetime]:
        """When the secret was last updated, in UTC.

        :returns: When the secret was last updated, in UTC.
        :rtype: ~datetime.datetime or None
        """
        return self._attributes.updated if self._attributes else None

    @property
    def recoverable_days(self) -> Optional[int]:
        """The number of days the key is retained before being deleted from a soft-delete enabled Key Vault.

        :returns: The number of days the key is retained before being deleted from a soft-delete enabled Key Vault.
        :rtype: int or None
        """
        # recoverable_days was added in 7.1-preview
        if self._attributes and hasattr(self._attributes, "recoverable_days"):
            return self._attributes.recoverable_days
        return None

    @property
    def recovery_level(self) -> Optional[str]:
        """The vault's deletion recovery level for secrets.

        :returns: The vault's deletion recovery level for secrets.
        :rtype: str or None
        """
        return self._attributes.recovery_level if self._attributes else None

    @property
    def vault_url(self) -> Optional[str]:
        """URL of the vault containing the secret.

        :returns: URL of the vault containing the secret.
        :rtype: str or None
        """
        return self._vault_id.vault_url if self._vault_id else None

    @property
    def name(self) -> Optional[str]:
        """The secret's name.

        :returns: The secret's name.
        :rtype: str or None
        """
        return self._vault_id.name if self._vault_id else None

    @property
    def version(self) -> Optional[str]:
        """The secret's version.

        :returns: The secret's version.
        :rtype: str or None
        """
        return self._vault_id.version if self._vault_id else None

    @property
    def tags(self) -> Optional[Dict[str, str]]:
        """Application specific metadata in the form of key-value pairs.

        :returns: A dictionary of tags attached to this secret.
        :rtype: dict or None
        """
        return self._tags

    @property
    def managed(self) -> Optional[bool]:
        """Whether the secret's lifetime is managed by Key Vault. If the secret backs a certificate, this will be true.

        :returns: True if the secret's lifetime is managed by Key Vault; False otherwise.
        :rtype: bool or None
        """
        return self._managed


class KeyVaultSecret(object):
    """All of a secret's properties, and its value.

    :param properties: The secret's properties.
    :type properties: ~azure.keyvault.secrets.SecretProperties
    :param value: The value of the secret.
    :type value: str or None
    """

    def __init__(self, properties: SecretProperties, value: Optional[str]) -> None:
        self._properties = properties
        self._value = value

    def __repr__(self) -> str:
        return f"<KeyVaultSecret [{self.id}]>"[:1024]

    @classmethod
    def _from_secret_bundle(cls, secret_bundle: _models.SecretBundle) -> "KeyVaultSecret":
        return cls(
            properties=SecretProperties._from_secret_bundle(secret_bundle),  # pylint: disable=protected-access
            value=secret_bundle.value,
        )

    @property
    def name(self) -> Optional[str]:
        """The secret's name.

        :returns: The secret's name.
        :rtype: str or None
        """
        return self._properties.name

    @property
    def id(self) -> Optional[str]:
        """The secret's ID.

        :returns: The secret's ID.
        :rtype: str or None
        """
        return self._properties.id

    @property
    def properties(self) -> SecretProperties:
        """The secret's properties.

        :returns: The secret's properties.
        :rtype: ~azure.keyvault.secrets.SecretProperties
        """
        return self._properties

    @property
    def value(self) -> Optional[str]:
        """The secret's value.

        :returns: The secret's value.
        :rtype: str or None
        """
        return self._value


class KeyVaultSecretIdentifier(object):
    """Information about a KeyVaultSecret parsed from a secret ID.

    :param str source_id: the full original identifier of a secret

    :raises ValueError: if the secret ID is improperly formatted

    Example:
        .. literalinclude:: ../tests/test_parse_id.py
            :start-after: [START parse_key_vault_secret_id]
            :end-before: [END parse_key_vault_secret_id]
            :language: python
            :caption: Parse a secret's ID
            :dedent: 8
    """

    def __init__(self, source_id: str) -> None:
        self._resource_id = parse_key_vault_id(source_id)

    @property
    def source_id(self) -> str:
        return self._resource_id.source_id

    @property
    def vault_url(self) -> str:
        return self._resource_id.vault_url

    @property
    def name(self) -> str:
        return self._resource_id.name

    @property
    def version(self) -> Optional[str]:
        return self._resource_id.version


class DeletedSecret(object):
    """A deleted secret's properties and information about its deletion.

    If soft-delete is enabled, returns information about its recovery as well.

    :param properties: The deleted secret's properties.
    :type properties: ~azure.keyvault.secrets.SecretProperties
    :param deleted_date: When the secret was deleted, in UTC.
    :type deleted_date: ~datetime.datetime or None
    :param recovery_id: An identifier used to recover the deleted secret.
    :type recovery_id: str or None
    :param scheduled_purge_date: When the secret is scheduled to be purged by Key Vault, in UTC.
    :type scheduled_purge_date: ~datetime.datetime or None
    """

    def __init__(
        self,
        properties: SecretProperties,
        deleted_date: Optional[datetime] = None,
        recovery_id: Optional[str] = None,
        scheduled_purge_date: Optional[datetime] = None,
    ) -> None:
        self._properties = properties
        self._deleted_date = deleted_date
        self._recovery_id = recovery_id
        self._scheduled_purge_date = scheduled_purge_date

    def __repr__(self) -> str:
        return f"<DeletedSecret [{self.id}]>"[:1024]

    @classmethod
    def _from_deleted_secret_bundle(cls, deleted_secret_bundle: _models.DeletedSecretBundle) -> "DeletedSecret":
        return cls(
            properties=SecretProperties._from_secret_bundle(deleted_secret_bundle),  # pylint: disable=protected-access
            deleted_date=deleted_secret_bundle.deleted_date,
            recovery_id=deleted_secret_bundle.recovery_id,
            scheduled_purge_date=deleted_secret_bundle.scheduled_purge_date,
        )

    @classmethod
    def _from_deleted_secret_item(cls, deleted_secret_item: _models.DeletedSecretItem) -> "DeletedSecret":
        return cls(
            properties=SecretProperties._from_secret_item(deleted_secret_item),  # pylint: disable=protected-access
            deleted_date=deleted_secret_item.deleted_date,
            recovery_id=deleted_secret_item.recovery_id,
            scheduled_purge_date=deleted_secret_item.scheduled_purge_date,
        )

    @property
    def name(self) -> Optional[str]:
        """The secret's name.

        :returns: The secret's name.
        :rtype: str or None
        """
        return self._properties.name

    @property
    def id(self) -> Optional[str]:
        """The secret's ID.

        :returns: The secret's ID.
        :rtype: str or None
        """
        return self._properties.id

    @property
    def properties(self) -> SecretProperties:
        """The properties of the deleted secret.

        :returns: The properties of the deleted secret.
        :rtype: ~azure.keyvault.secrets.SecretProperties
        """
        return self._properties

    @property
    def deleted_date(self) -> Optional[datetime]:
        """When the secret was deleted, in UTC.

        :returns: When the secret was deleted, in UTC.
        :rtype: ~datetime.datetime or None
        """
        return self._deleted_date

    @property
    def recovery_id(self) -> Optional[str]:
        """An identifier used to recover the deleted secret.

        :returns: An identifier used to recover the deleted secret.
        :rtype: str or None
        """
        return self._recovery_id

    @property
    def scheduled_purge_date(self) -> Optional[datetime]:
        """When the secret is scheduled to be purged by Key Vault, in UTC.

        :returns: When the secret is scheduled to be purged by Key Vault, in UTC.
        :rtype: ~datetime.datetime or None
        """
        return self._scheduled_purge_date
