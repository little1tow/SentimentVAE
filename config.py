# flake8: noqa
import os
import tensorflow as tf

flags = tf.flags
cfg = flags.FLAGS


# command-line config
flags.DEFINE_string ("data_path",  "data/yelp",          "Data path")
flags.DEFINE_string ("save_file",  "models/recent.dat",  "Save file")
flags.DEFINE_string ("load_file",  "",                   "File to load model from")
flags.DEFINE_string ("vocab_file", "vocab",              "Vocab pickle file")
flags.DEFINE_float  ("keep_fraction",   0.97,            "Percentage of vocab to keep")

flags.DEFINE_integer("batch_size",      48,      "Batch size")
flags.DEFINE_bool   ("group_length",    True,    "Whether to group similar length "
                                                 "sentences")
flags.DEFINE_integer("max_length",      None,    "The maximum length of sentences in "
                                                 "the dataset")
flags.DEFINE_integer("word_emb_size",   224,     "Number of learnable dimensions in "
                                                 "word embeddings")
flags.DEFINE_integer("label_emb_size",  3,       "Number of learnable dimensions in "
                                                 "label embeddings")
flags.DEFINE_bool   ("use_labels",      False,   "Use labels to condition on")
flags.DEFINE_bool   ("autoencoder",     True,    "Use an encoder (disable for pure LM)")
flags.DEFINE_bool   ("variational",     True,    "Use variational objective")
flags.DEFINE_bool   ("mutual_info",     True,    "Use mutual information objective")
flags.DEFINE_bool   ("decoder_inputs",  True,    "Give true data as input to decoder")
flags.DEFINE_bool   ("encoder_birnn",   True,    "Encoder is bidirectional")
flags.DEFINE_bool   ("convolutional",   False,   "Use convolutional encoder instead of "
                                                 "RNN")
flags.DEFINE_string ("conv_width",      '5,5,3', "Convolutional kernel widths per layer")
flags.DEFINE_string ("encoder_summary", 'mean',  "How to use encoder states "
                                                 "(laststate, mean, attention)")
flags.DEFINE_integer("num_layers",      1,       "Number of RNN layers")
flags.DEFINE_integer("max_gen_length",  50,      "Maximum length of generated sentences")
flags.DEFINE_integer("beam_size",       16,      "Beam size for beam search")
flags.DEFINE_integer("hidden_size",     512,     "RNN hidden state size")
flags.DEFINE_integer("latent_size",     64,      "Latent representation size")
flags.DEFINE_integer("dropout_start",   4000,    "Start reducing dropout at this step")
flags.DEFINE_integer("dropout_finish",  13000,   "Stop reducing dropout at this step")
flags.DEFINE_float  ("init_dropout",    0.95,    "Initial word dropout probability for "
                                                 "decoder input")
flags.DEFINE_float  ("word_dropout",    0.2,     "Final word dropout probability for "
                                                 "decoder input")
flags.DEFINE_float  ("decoding_noise",  0.1,     "StdDev of added noise to states during "
                                                 "beam search decoding (-1 to disable)")
flags.DEFINE_float  ("length_penalty",  100.0,   "Bias beamsearch logprobs by "
                                                 "lp * log(curlen / targetlen)")
flags.DEFINE_integer("softmax_samples", 1000,    "Number of classes to sample for "
                                                 "softmax")
flags.DEFINE_integer("val_ll_samples",  3,       "Number of samples to use to estimate "
                                                 "log-likelihood of validation data")
flags.DEFINE_integer("test_ll_samples", 6,       "Number of samples to use to estimate "
                                                 "log-likelihood of test data")
flags.DEFINE_float  ("max_grad_norm",   5.0,     "Gradient clipping")
flags.DEFINE_integer("anneal_bias",     6500,    "The step to reach ~1.0 for KL "
                                                 "divergence weight annealing. Set to 0 to"
                                                 "disable annealing and set KLD weight to"
                                                 "anneal_max from the start.")
flags.DEFINE_float  ("anneal_max",      1.0,     "The maximum KL divergence weight")
flags.DEFINE_float  ("mutinfo_weight",  1.0,     "The weight for the mutual info cost")
flags.DEFINE_bool   ("training",        True,    "Training mode, turn off for testing")
flags.DEFINE_string ("optimizer",       "adam",  "Optimizer to use (sgd, adam, adagrad, "
                                                 "adadelta)")
flags.DEFINE_float  ("learning_rate",   1e-3,    "Optimizer initial learning rate")
flags.DEFINE_integer("max_epoch",       10000,   "Maximum number of epochs to run for")
flags.DEFINE_integer("max_steps",       9999999, "Maximum number of steps to run for")

flags.DEFINE_integer("print_every",     50,      "Print every these many steps")
flags.DEFINE_integer("display_every",   0,       "Print generated sentences every these "
                                                 "many steps")
flags.DEFINE_integer("save_every",      -1,      "Save every these many steps (0 to "
                                                 "disable, -1 for each epoch)")
flags.DEFINE_bool   ("save_overwrite",  True,    "Overwrite the same file each time")
flags.DEFINE_bool   ("test_validation", True,    "Use the validation set during testing")
flags.DEFINE_integer("validate_every",  1,       "Validate every these many epochs (0 "
                                                 "to disable)")
flags.DEFINE_bool   ("debug",           False,   "Debug mode")
flags.DEFINE_integer("gpu_id",          -1,      "The GPU to use (-1 for default)")


if cfg.gpu_id != -1:
    os.environ['CUDA_VISIBLE_DEVICES'] = str(cfg.gpu_id)

print('Config:')
cfg._parse_flags()
cfg_dict = cfg.__dict__['__flags']
maxlen = max(len(k) for k in cfg_dict)
for k, v in sorted(cfg_dict.items(), key=lambda x: x[0]):
    print(k.ljust(maxlen + 2), v)
print()
