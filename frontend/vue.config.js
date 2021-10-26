module.exports = {
    css: {
        loaderOptions: {
            sass: {
                prependData: `
                    @import "@/assets/scss/_variables.scss";
                    @import "@/assets/scss/_global.scss";
                    @import "@/assets/scss/_transition_classes.scss";
                `
            }
        }
    },
    assetsDir: 'static',
}