<template>
    <div class="container">
        <router-view/>
    </div>
</template>

<style scoped>
.container {
    background: #6C3F5E;
    min-height: 100vh;
    min-width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
button:active, button:focus, input:active, input:focus, textarea:active, textarea:focus {
  outline: none;
}
button::-moz-focus-inner, input::-moz-focus-inner, textarea::-moz-focus-inner {
  border: 0;
}
</style>