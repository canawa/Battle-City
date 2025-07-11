<script setup>

</script>

<template>
<div id="main">
    <div> <img src='@/assets/split_or_steal.png' alt='split_or_steal' id='split_or_steal_image'> </div>
</div>
</template>

<style scoped>
#main {
    display: flex;
    justify-content: left;
    align-items: left;
    width: 100%;
    /* background-color: #09a24e; */
    padding: 1rem;
}

#split_or_steal_image {
    width: 40%;
    border-radius: 1rem;
}

@media (max-width: 768px) {
    #split_or_steal_image {
        width: 100%;
    }
}


</style>