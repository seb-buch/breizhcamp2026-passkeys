<script>
	import { Slide, SpeakerNotes, VerticalSpacer } from '@seb-buch/slyd';
</script>

<Slide>
	<h3>Passkeys : liées ou synchronisées ?</h3>
	<VerticalSpacer height="2em" />
	<table>
		<thead>
			<tr>
				<th></th>
				<th>🔒 Liées à l'appareil</th>
				<th>☁️ Synchronisées</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td class="label">Stockage</td>
				<td>Puce sécurisée (TEE / TPM)</td>
				<td>Cloud de l'écosystème</td>
			</tr>
			<tr>
				<td class="label">Exportable</td>
				<td class="pro">Non</td>
				<td>Dans l'écosystème</td>
			</tr>
			<tr>
				<td class="label">Perte d'appareil</td>
				<td class="con">Passkey perdue</td>
				<td class="pro">Récupérable</td>
			</tr>
			<tr>
				<td class="label">Niveau de sécurité</td>
				<td class="pro">Très élevé</td>
				<td>Élevé</td>
			</tr>
			<tr>
				<td class="label">Cas d'usage</td>
				<td>Clés matérielles (YubiKey…)</td>
				<td>Grand public</td>
			</tr>
		</tbody>
	</table>

	<SpeakerNotes>
		La spec WebAuthn distingue deux grandes familles de passkeys selon l'endroit où la clé privée
		est stockée. Les passkeys liées à l'appareil — single-device credentials — stockent la clé dans
		une puce sécurisée, TEE ou TPM selon le matériel. La clé ne quitte jamais le hardware : c'est le
		niveau de sécurité maximal, utilisé notamment par les clés physiques comme les YubiKey. Mais si
		l'appareil est perdu ou cassé, la passkey est définitivement perdue.<br />
		Les passkeys synchronisées — multi-device credentials — délèguent le stockage au cloud de l'écosystème
		: iCloud Keychain chez Apple, Google Password Manager chez Google. La clé privée est chiffrée et synchronisée
		entre vos appareils. En cas de perte, vous récupérez vos passkeys en vous reconnectant à votre compte.
		C'est beaucoup plus confortable pour le grand public.<br />
		Côté implémentation, c'est le paramètre <code>authenticatorAttachment</code> dans les options
		WebAuthn qui pilote ce comportement : <code>platform</code> pour les passkeys synchronisées,
		<code>cross-platform</code> pour les passkeys liées à l'appareil. Dans la grande majorité des
		applications grand public, vous voudrez <code>platform</code> — ou laisser l'utilisateur choisir.
	</SpeakerNotes>
</Slide>

<style>
	table {
		box-shadow: none;
		text-align: center;
	}

	th {
		background: transparent;
		color: var(--r-heading-color);
		border-bottom: 2px solid var(--dvx-orange);
	}

	td {
		background: transparent !important;
		border-bottom: 1px solid rgba(0, 0, 0, 0.08);
	}

	tr:hover td {
		background: transparent !important;
	}

	.label {
		font-weight: 700;
		color: var(--ocean-deep);
	}

	.pro {
		color: var(--sea-green);
	}

	.con {
		color: var(--danger-red);
	}
</style>
