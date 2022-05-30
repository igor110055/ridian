<template>
  <div id="app">
    <div class="assessment-container container">
      <!-- <router-link :to="'/'" class="router_link"
        >Pay With Binance Wallet
      </router-link> -->
      <router-link
        :to="'/withdrawals'"
        class="router_link"
        style="margin-left: 10px"
        >Withdraw
      </router-link>
      <router-link
        :to="'/convert'"
        class="router_link"
        style="margin-left: 10px"
        >Convert
      </router-link>

      <dir class="container">
        <div class="row">
          <div class="col-md-6" style="margin-top: 50px">
            <span style="font-size: 20px">Ridian Share available</span>
            <div class="progress">
              <div
                class="progress-bar"
                role="progressbar"
                v-bind:style="fullWidth"
                :aria-valuenow="width"
                aria-valuemin="0"
                :aria-valuemax="totalamount"
              >
                {{ width }}/{{ totalamount }}
              </div>
            </div>
          </div>
        </div>
      </dir>

      <h5 style="margin-right: 890px">
        Ridian share Ratio <br />
        1 USDC = 2 Ridian Shares
      </h5>

      <!-- <h3 style="position: absolute">
        Remaing shares MATIC ( <b>{{ shares }}</b> )
      </h3> -->

      <div class="row" style="margin-top: -70px">
        <div class="col-md-6 form-box">
          <div v-show="show1">
            <div class="form-top">
              <div class="form-top-left">
                <h3 class="text-left">Buy Ridian Shares</h3>
                <!-- <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit
                                </p> -->
              </div>
            </div>
            <div class="form-bottom">
              <div class="form-group">
                <label for="">Email</label>
                <input
                  type="email"
                  v-model="user.email"
                  name="amount"
                  placeholder="Email"
                  class="form-email form-control"
                  id="amount"
                  required
                />
              </div>
              <!-- <div class="form-group">
                                <label for="">Api Key</label>
                                <input type="text"  v-model="user.api_key" name="amount" placeholder="Api Key" class="form-email form-control" id="amount" required>
                            </div>
                            <div class="form-group">
                                <label for="">Seceret Key</label>
                                <input type="text"  v-model="user.seceret_key" name="amount" placeholder="Seceret Key" class="form-email form-control" id="amount" required>
                            </div> -->
              <div class="form-group">
                <label for=""> Asset type</label>
                <select class="form-control" v-model="user.coin">
                  <option>MATIC</option>
                    <option>BTC</option>
                      <option>ETH</option>
                       <option>SOL</option>
                      

                </select>
              </div>
              <div class="row">
                <div class="form-group col-md-6">
                  <label for="">Amount</label>
                  <input
                    type="number"
                    v-model="amount"
                    name="amount"
                    placeholder="Amount"
                    class="form-email form-control"
                    id="amount"
                    required
                  />
                </div>
                <div class="form-group col-md-6">
                  <label for="">Ridian Shares</label>
                  <input
                    readonly
                    type="number"
                    v-model="ridianShares"
                    name="amount"
                    placeholder="Ridian Shares"
                    class="form-email form-control"
                    id="amount"
                    required
                  />
                </div>
              </div>

              <button type="button" @click="submit()" class="btn btn-next mt-3">
                Deposit
              </button>
              <span
                style="
                  position: relative;
                  font-size: 18px;
                  top: 54px;
                  right: 93px;
                "
                >User Share balance ({{ userRidianshare }})</span>
              <br />
            </div>

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
      amount: "",
      totalamount: "",
      userRidianshare: "",
      show: false,
      width: 0,
      show1: true,
      ridianShares: "",
      shares: "",
      user: {
        api_key: "",
        seceret_key: "",
        amount: "",
        coin: "",
        email: "",
      },
    };
  },
  watch: {
    amount(val) {

      if(val >=1 && val <=1000 )
      {
         this.ridianShares = val * 2;
      }
      else if(val == '')
      {
         this.ridianShares=''
      }
      else
      {
       alert("Amount Between 1 And 1000")
      }
     
      //this.inputted = `Inputted: ${val}`;
    },
  },
  computed: {
    fullWidth() {
      return `width:${this.width}%`;
    },
  },
  mounted() {
    const path = "http://127.0.0.1:5000/detail";
    axios
      .get(path)
      .then((response) => {
        this.width = response.data.ridian_shares;
        this.totalamount = response.data.total_ridian_shares;
        this.shares = response.data.ridian_shares;
        this.userRidianshare = response.data.user_ridian_shares;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  methods: {
    previous: function () {
      (this.show1 = true), (this.show = false);
    },
    next: function () {
      (this.show1 = false), (this.show = true);
    },
    submit: function () {
      const path = "http://127.0.0.1:5000/dataentry";
      axios
        .post(path, {
          api_key: " this.user.api_key",
          seceret_key: "this.user.seceret_key",
          amount: this.amount,
          coin: "MATIC",
          email: "this.user.email",
        })
        .then((response) => {
          this.amount = "";
          this.user.coin = "";
          this.user.email = "";
          console.log(response);
          alert(response.data.message);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

