<template>
  <div id="app">
    <div class="assessment-container container">

      <router-link :to="'/'" class="router_link">FTX Wallet </router-link>

      <!-- <button class="mt-4">Pay With FTX Wallet</button>
         <button class="mt-4" style="margin-left:10px">Pay With Binance Wallet</button> -->
      <div class="row">
        <div class="col-md-6 form-box">

          <div class="form-top">
            <div class="form-top-left">
              <h3 class="text-left">Ridian share to Token</h3>
              <!-- <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit
                                </p> -->
            </div>
          </div>
          <div class="form-bottom">
            <!-- <div class="form-group">
                                <label for="">Address</label>
                                <input type="text" readonly  v-model="user.address" name="amount"  class="form-email form-control" id="amount" required>
                            </div> -->
            <div class="form-group">
              <label for=""> Asset type</label>
              <select class="form-control" v-model="user.coin">
                <!-- <option selected>ETHRIUM</option>
                                    <option>BTC</option> -->
                <option>USDC</option>
              </select>
            </div>
            <div class="row">

              <div class="form-group col-md-6">
                <label for="">Ridian Shares</label>
                <input type="number" v-model="shares" name="amount" placeholder="Amount" class="form-email form-control"
                  id="amount" required>


              </div>

              <div class="form-group col-md-6">
                <label for="">USDC Amount</label>
                <input type="number" readonly v-model="res" name="amount" placeholder="Matic Amount"
                  class="form-email form-control" id="amount" required>



              </div>

            </div>
            <div class="row">
              <div class="col-md-12">
                <button type="button" @click="instant()" class="btn btn-next mt-3 m-1">
                  Instant Convert</button>

                <button type="button" @click="delay()" class="btn btn-next mt-3 m-1">
                  Delay Convert (24hrs)</button>
              </div>

            </div>
            <!-- <button type="button" @click="submit()" class="btn btn-next mt-3">convert</button> -->
            <span style="
                  position: relative;
                  font-size: 18px;
                  top: 6px;
                  right: -4px;
                ">User Share balance ({{ userRidianshare }})


            </span><br><br>
            <span style="font-size:18px"> Instant Convert = 0.3% fee</span>
            <br>
            <span style="font-size:18px">Delay Convert 24hrs = Free</span>

            <br />
          </div>


        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      userRidianshare: '',
      matic_amount: '',
      ridian_shares: '',
      shares: '',
      res: '',
      user: {

        amount: "",
        coin: "",
      },
    };
  },
  watch: {
    shares(val) {


      this.res = val / 2
    },

  },
  mounted() {
    const path = "http://127.0.0.1:5000/detail";
    axios
      .get(path)
      .then((response) => {
        this.userRidianshare = response.data.user_ridian_shares;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  methods: {

    // submit: function () {
    //   const path = "http://127.0.0.1:5000/convert";
    //   axios
    //     .post(path, {

    //       amount: this.shares,
    //       coin: this.user.coin,
    //     })
    //     .then((response) => {
    //       this.shares = ''
    //       this.user.coin = ''
    //       alert(response.data.message);
    //     })
    //     .catch((err) => {
    //       console.log(err);
    //     });
    // },

    instant: function () {
      const path = "http://127.0.0.1:5000/convert";
      axios
        .post(path, {

          amount: this.shares,
          coin: this.user.coin,
          type: 'instant'
        })
        .then((response) => {
          this.shares = ''
          this.user.coin = ''
          alert(response.data.message);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    delay: function () {
      const path = "http://127.0.0.1:5000/convert";
      axios
        .post(path, {

          amount: this.shares,
          coin: this.user.coin,
          type: 'delay'
        })
        .then((response) => {
          this.shares = ''
          this.user.coin = ''
          alert(response.data.message);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>
