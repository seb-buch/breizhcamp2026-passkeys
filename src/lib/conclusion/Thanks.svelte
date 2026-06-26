<script>
	import { QRCode, Slide, SpeakerNotes } from '@seb-buch/slyd';
	import photo from '$lib/assets/images/sebastien-buchoux.jpg';
	import onepointLogo from '$lib/assets/images/onepoint_logo.png';
	import background from '$lib/assets/images/background-title.png';

	const url = 'https://seb-buch.github.io/breizhcamp2026-passkeys/links';
</script>

<Slide backgroundImage={background} backgroundSize="cover">
	<div class="thanks-overlay">
		<div class="who-i-am">
			<figure class="who-photo">
				<img src={photo} alt="Sébastien Buchoux" />
			</figure>
			<ul class="who-info">
				<li class="who-name">Sébastien Buchoux</li>
				<li>Tech Lead / Architecte Logiciel</li>
				<li class="who-company">
					<img src={onepointLogo} alt="Onepoint" class="who-company-logo" />
				</li>
				<li>
					<a href="https://github.com/seb-buch" target="_blank" rel="noopener">
						<i class="fa-brands fa-github" style="color: var(--r-main-color)"></i> seb-buch
					</a>
				</li>
				<li>
					<a href="https://www.linkedin.com/in/sebastien-buchoux/" target="_blank" rel="noopener">
						<i class="fa-brands fa-linkedin" style="color: var(--r-main-color)"></i>
						sebastien-buchoux
					</a>
				</li>
			</ul>
		</div>
		<div class="thanks">
			<h1>Merci !</h1>
			<h3>Questions ?</h3>
		</div>
		<div class="qr-code">
			<QRCode {url} shape="circle" legend="Diapos / Code / Feedback" size="300px" />
		</div>
	</div>
	<SpeakerNotes>
		Et voilà, c'est terminé ! Merci beaucoup pour votre attention. Si vous avez des questions, c'est
		le moment. N'hésitez pas à venir me voir après la session aussi, et à jeter un œil au repo pour
		expérimenter avec les passkeys par vous-mêmes. Merci !
	</SpeakerNotes>
</Slide>

<style>
	.thanks-overlay {
		display: flex;
		flex-direction: row;
		justify-content: space-around;
		height: 100%;
		align-items: center;
		gap: 2em;
		background: #f1f5f8bb;
		backdrop-filter: blur(10px);
		border-radius: 10px;
		padding: 20px;
		box-sizing: border-box;

		.who-i-am {
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: center;
			gap: 1em;

			.who-photo img {
				width: 250px;
				height: 250px;
				border-radius: 50%;
				object-fit: cover;
				border: 4px solid var(--slyd-accent-color);
				box-shadow: 0 4px 24px rgba(0, 0, 0, 0.12);
			}

			.who-info {
				list-style: none;
				padding: 0;
				margin: 0;
				text-align: left;
				font-size: 0.9em;
				display: flex;
				flex-direction: column;
				gap: 0.4em;
				align-items: center;

				li {
					margin-bottom: 0.3em;
					display: flex;
					align-items: center;
					gap: 0.4em;

					&::before {
						display: none;
					}
				}
			}

			.who-name {
				font-size: 1.3em;
				font-weight: bold;
				color: var(--slyd-accent-color);
				font-family: var(--slyd-headings-font), sans-serif;
			}

			.who-company {
				text-align: center;
			}

			.who-company-logo {
				height: 2em;
				border-radius: 6px;
				vertical-align: middle;
				margin: 0;
			}

			.who-info a {
				text-decoration: none;
				transition: color 0.2s ease;
			}
		}

		.thanks {
			h1 {
				margin-bottom: 1em;
			}

			h3 {
				border: none;
				text-align: center;
			}
		}
	}
</style>
