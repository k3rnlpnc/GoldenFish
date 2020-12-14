<template>
    <div class="spinner-cube">
        <div></div>
        <div></div>
    </div>
</template>

<style scoped>
.spinner-cube
{
    width: 60px;
    height: 60px;
    position: relative;
}

.spinner-cube > div
{
    background-color: #6C3F5E;
    width: 20px;
    height: 20px;
    position: absolute;
    top: 0;
    left: 0;

    -webkit-animation: cuberotate 1.8s infinite ease-in-out;
    animation: cuberotate 1.8s infinite ease-in-out;
}

.spinner-cube div:nth-child(2)
{
    -webkit-animation-delay: -0.9s;
    animation-delay: -0.9s;
}

@-webkit-keyframes cuberotate {
    25% { -webkit-transform: translateX(22px) rotate(-90deg) scale(0.5) }
    50% { -webkit-transform: translateX(22px) translateY(22px) rotate(-180deg) }
    75% { -webkit-transform: translateX(0px) translateY(22px) rotate(-270deg) scale(0.5) }
    100% { -webkit-transform: rotate(-360deg) }
}

@keyframes cuberotate {
    25% { transform: translateX(42px) rotate(-90deg) scale(0.5); }
    50% { transform: translateX(42px) translateY(42px) rotate(-179deg); }
    50.1% { transform: translateX(42px) translateY(42px) rotate(-180deg); }
    75% { transform: translateX(0px) translateY(42px) rotate(-270deg) scale(0.5); }
    100% { transform: rotate(-360deg); }
}
</style>