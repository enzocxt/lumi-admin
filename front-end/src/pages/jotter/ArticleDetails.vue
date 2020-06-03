<template>
  <div class="articles-area">
    <el-card style="text-align: left;width: 990px;margin: 35px auto 0 auto">
      <div>
        <span style="font-size: 20px">
          <strong>{{ article.articleTitle }}</strong>
        </span>
        <el-divider content-position="left">
          {{ article.articleDate }}
        </el-divider>
        <div class="markdown-body">
          <div v-html="article.articleContentHtml"></div>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'ArticleDetails',
  data () {
    return {
      article: []
    }
  },
  mounted () {
    this.loadArticle()
  },
  methods: {
    loadArticle () {
      // api[GET]: /api/article/<id>
      var _this = this
      this.$axios.get(`/article/${this.$route.query.id}`)
        .then(resp => {
          console.log('article response:', resp)
          if (resp && resp.status === 200) {
            // _this.article = resp.data
            // re-format article
            let ele = resp.data
            let tmp = {
              id: -1,
              articleTitle: '',
              articleContentHtml: '',
              articleAbstract: '',
              articleCover: '',
              articleDate: '',
            }
            tmp.id = ele.id
            tmp.articleTitle = ele.article_title
            tmp.articleContentHtml = ele.article_content_html
            tmp.articleAbstract = ele.article_abstract
            tmp.articleCover = ele.article_cover
            tmp.articleDate = ele.article_date
            _this.article = tmp
          }
        })
    }
  }
}
</script>

<style scoped>
@import "../../styles/markdown.css";
</style>

