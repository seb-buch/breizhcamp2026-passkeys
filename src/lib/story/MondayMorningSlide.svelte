<script lang="ts">
	import { Slide, SpeakerNotes } from '@seb-buch/slyd';
	import backgroundImage from '$lib/story/images/monday_morning.png';
	import { fly } from 'svelte/transition';

	type Props = {
		legend?: string;
	};

	const { legend }: Props = $props();
</script>

<Slide {backgroundImage} backgroundSize="cover">
	{#if legend}
		<p class="animated-legend" in:fly={{ y: 180, duration: 500, delay: 400 }}>
			{legend}
		</p>
	{/if}
	<SpeakerNotes>
		<p>
			On est lundi matin.<br />
			Bob est content car il va pouvoir à nouveau cuisiner des patés de crabe.<br />
			C'est son activité préférée.<br />
		</p>
	</SpeakerNotes>
</Slide>
