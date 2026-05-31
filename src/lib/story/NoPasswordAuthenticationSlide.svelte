<script lang="ts">
	import { Slide, SpeakerNotes } from '@seb-buch/slyd';
	import backgroundImage from '$lib/story/images/no_password_authentication.png';
</script>

<Slide {backgroundImage} backgroundSize="cover">
	<div class="section-title fragment">
		<h2>Comment s'authentifier sans mot de passe&nbsp;?</h2>
	</div>
	<SpeakerNotes>
		<p>TODO</p>
	</SpeakerNotes>
</Slide>

<style>
	.section-title {
		height: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
		width: 100%;
		background: #f1f5f8bb;
		backdrop-filter: blur(10px);
		border-radius: 10px;
		padding: 20px;
		box-sizing: border-box;
	}
</style>
